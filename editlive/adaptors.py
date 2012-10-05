import re

from django.utils.safestring import mark_safe
from django.forms import ValidationError
from django.forms.models import modelform_factory
from django.forms import ModelForm

from editlive.utils import get_dict_from_obj, apply_filters, import_class


class BaseAdaptor(object):

    def __init__(self, field, obj, field_name, field_value=None, kwargs={}, initial={}):
        self.kwargs = kwargs
        self.field = field
        self.obj = obj
        self.model = obj.__class__
        self.field_name = field_name
        self.field_value = field_value
        self.template_filters = None
        self.form_class = modelform_factory(self.model)
        self.form = self.form_class(instance=self.obj, initial=initial)
        self.form_field = self.form[self.field_name]

        if self.kwargs.get('formset'):
            self.field_index = self.kwargs.get('field-index', 0)
            self.field_name = '%s_set-%d-%s' % (
                                self.kwargs.get('formset'), 
                                self.field_index, 
                                self.form_field.html_name)
            self.field_id = 'id_%s' % self.field_name
        else:
            self.field_id = self.form_field.auto_id

        self.attributes = {
            'data-type': 'livetextField',
            'data-field-id': self.field_id,
            'module-name': self.model._meta.module_name,
            'app-label': self.model._meta.app_label,
            'field-name': self.field_name,
            'object-id': self.obj.pk,
            'rendered-value': 'Cliquer pour modifier',
        }

        if self.kwargs.get('template_filters'):
            self.template_filters = self.kwargs.get('template_filters').split('|')

    def format_attributes(self):
        o = []
        for k, v in self.kwargs.items():
            if k == 'template_filters':
                self.attributes['rendered-value'] = self.get_value()
                self.attributes[k] = v
            elif v is not None:
                self.attributes['data-' + k] = v

        for k, v in self.attributes.items():
            if v is not None:
                o.append('%s="%s"' % (k, v))
        return ' ' + ' '.join(o) + ' '

    def get_value(self):
        return self.render_value()

    def set_value(self, value):
        self.field_value = value
        setattr(self.obj, self.field_name, self.field_value)
        return value

    def save(self):
        form = self.get_form()
        if form.is_valid():
            self.obj.save()
            return {
                'error': False,
                'rendered_value': self.render_value()}
        else: 
            messages = []
            for field_name_error, errors_field in form.errors.items():
                for error in errors_field:
                    messages.append({'field_name': field_name_error, 'message': unicode(error)})

            return {
                'error': True, 
                'messages': messages,
                'rendered_value': self.render_value()}

    def render_widget(self):
        self.attributes['rendered-value'] = self.render_value()
        return u'<editlive%s/>' % self.format_attributes()

    def render(self):
        field = unicode(self.form_field)
        
        if self.kwargs.get('formset'):
            auto_id = 'id="%s"' % self.form_field.auto_id
            name = 'name="%s"' % self.form_field.html_name
            field = re.sub(auto_id, 'id="%s"' % self.field_id, field)
            field = re.sub(name, 'name="%s"' % self.field_name, field)

        return mark_safe(field + self.render_widget())

    def render_value(self, value=None):
        value = value or self.field_value
        if callable(value): value = value()
        return apply_filters(value, self.template_filters)

    def get_form(self):
        form = modelform_factory(self.model)
        return form(data=get_dict_from_obj(self.obj), instance=self.obj)


class TextAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(TextAdaptor, self).__init__(*args, **kwargs)
        self.attributes.update({'data-type': 'textField'})


class BooleanAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(BooleanAdaptor, self).__init__(*args, **kwargs)
        self.attributes.update({'data-type': 'booleanField'})

    def set_value(self, value):
        self.field_value = value
        setattr(self.obj, self.field_name, self.field_value)
        return value


class DateAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(DateAdaptor, self).__init__(*args, **kwargs)
        self.attributes.update({'data-type': 'dateField'})


class DateTimeAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(DateTimeAdaptor, self).__init__(*args, **kwargs)
        self.attributes.update({'data-type': 'datetimeField'})


class ForeignKeyAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(ForeignKeyAdaptor, self).__init__(*args, **kwargs)
        self.attributes.update({
            'data-type':   'foreignkeyField',
            'data-source': '#%s' % self.attributes.get('data-field-id'),
        })

    def set_value(self, value):
        self.field_value = value
        setattr(self.obj, '%s_id' % self.field_name, self.field_value)
        return value

    def render_value(self):
        value = getattr(self.obj, self.field_name, None)
        if value:
            if callable(value): value = value()
            return unicode(apply_filters(value, self.template_filters))
        else:
            return u''


class ChoicesAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(ChoicesAdaptor, self).__init__(*args, **kwargs)
        self.attributes.update({'data-type': 'choicesField'})


class ManyToManyAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(ManyToManyAdaptor, self).__init__(*args, **kwargs)
        self.attributes.update({
            'data-type':   'manytomanyField',
            'data-source': '#%s' % self.attributes.get('data-field-id'),
        })

    def set_value(self, value):
        if value is None:
            self.field_value = []
            getattr(self.obj, self.field_name).clear()
        else:
            self.field_value = value
            setattr(self.obj, self.field_name, value)
        return value


def get_dynamic_modelform(**kwargs):
    form = type('DynamicForm',(ModelForm,),{})
    meta = type('Meta',(object,),{})
    meta.exclude = kwargs.get('exclude', None)
    form.Meta = meta
    return form

class BaseInlineAdaptor(object):

    def __init__(self, obj, manager, value, initial={}, **kwargs):
        self.kwargs = kwargs['kwargs']
        self.manager_name = manager
        self.manager = getattr(obj, manager)
        self.model = self.manager.model
        self.obj = self.model()
        self.value = value
        # TODO: fix this shit..
        # http://stackoverflow.com/questions/12462616/finding-the-relation-field-of-a-related-object-in-django
        self.query_field = self.manager.core_filters.keys()[0].split('__')[0]
        self.form_class = self.get_form()
        self.initial = initial
        self.initial[self.query_field] = obj.pk

        self.form = self.form_class(**{
            'instance': self.obj, 
            'initial': initial,
            'prefix': self.manager_name[:-4],
        })

    def get_object_list(self):
        return self.manager.all()

    def get_form(self):
        fkwargs = {}
        if self.kwargs.get('form'):
            # Custom form
            fkwargs['form'] = import_class(self.kwargs.get('form'))
        else:
            # Generic form
            fkwargs['form'] = get_dynamic_modelform(exclude=(self.query_field,))

        return modelform_factory(self.model, **fkwargs)

    def render(self):
        return {
            'object_list': self.get_object_list(),
            'form': self.form,
        }


class TabularInlineAdaptor(BaseInlineAdaptor):
    pass


class StackedInlineAdaptor(BaseInlineAdaptor):
    pass