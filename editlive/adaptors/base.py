import re
from datetime import datetime

from django.utils.safestring import mark_safe
from django.forms.models import modelform_factory

from editlive.utils import (get_dict_from_obj,\
        apply_filters, import_class, get_dynamic_modelform)


class BaseAdaptor(object):
    """The BaseAdaptor is an abstract class which provides all the 
    basic methods and variable necessary to interact with and render 
    an object field.

    It provides the following functionalities:

    * Renders the object's display value (rendered with filters applied)
    * Renders the editlive markup
    * Get a field value
    * Set a field value
    * Validate field value
    * Save a field value

    .. envvar:: kwargs 

    .. note::

       This class is never used directly, you must subclass it.

    """

    def __init__(self, request, field, obj, field_name, field_value='', \
            kwargs={}):

        self.request = request 
        self.kwargs = kwargs
        self.field = field
        self.obj = obj
        self.model = obj.__class__
        self.field_name = field_name
        self.field_value = getattr(self.obj, self.field_name, field_value)
        self.template_filters = None
        self.load_tags = []
        self.form = self.get_form()

        try:
            self.form_field = self.form[self.field_name]
        except KeyError:
            self.form_field = False

        if self.form_field:
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
                self.template_filters = self.kwargs.get('template_filters')\
                                            .split('|')
                if self.kwargs.get('load_tags'):
                    self.load_tags = self.kwargs.get('load_tags').split('|')

    def can_edit(self):
        return self.request.user.is_authenticated()

    def format_attributes(self):
        """Formats the HTML attributes of the <editlive /> element.

        This method takes no argument, it only use `self.kwargs` to build up
        `self.attributes` then convert it to HTML attributes and return it as
        a string.

        >>> self.format_attributes()
        app-label="myapp" field-name="myfieldname"
        rendered-value="Hello World" object-id="1"
        data-type="charField" data-field-id="id_myfieldname"
        module-name="mymodule"

        Most kwargs are prefixed with `data-` when converted to attribute
        except for those:

        * rendered-value
        * load_tags

        """
        o = []
        for k, v in self.kwargs.items():
            if k == 'template_filters':
                self.attributes['rendered-value'] = self.render_value()
                self.attributes[k] = v
            elif k in ['load_tags']:
                self.attributes[k] = v
            elif v is not None and v not in ['readonly']:
                self.attributes['data-' + k] = v

        for k, v in self.attributes.items():
            if v is not None:
                o.append('%s="%s"' % (k, v))

        return ' ' + ' '.join(o) + ' '

    def get_form(self):
        """Creates and returns a form on the fly from the model using
        `modelform_factory`.

        The returned form is instantiated with `self.obj`.
        """
        if self.kwargs.get('form'):  # Custom form
            try:
                form = import_class(self.kwargs.get('form'))
            except ImportError:  # TODO: warning sent to logger or something ?
                form = modelform_factory(self.model)
        else:  # Generic form
            form = modelform_factory(self.model)
        return form(data=get_dict_from_obj(self.obj), instance=self.obj)

    def get_real_field_name(self):
        """Returns the reald fieldname regardless if the field is part of a
        formset or not.

        Formsets mangles fieldnames with positional slugs. This method 
        returns the actual field name without the position.

        >>> print self.field_name
        "myfieldname_set-0"
        >>> print self.get_real_field_name()
        "myfieldname"
        """
        if '_set-' in self.field_name:  # Formset field
            manager, pos, field_name = filter(None, \
                    re.split(r'(\w+)_set-(\d+)-(\w+)', self.field_name))
        else:
            field_name = self.field_name
        return field_name

    def get_value(self):
        """Returns `self.field_value` unless it is callable. If it is 
        callable, it calls it before returning the output.
        """
        if callable(self.field_value):
            return self.field_value()
        return self.field_value

    def set_value(self, value):
        """Set the value of the object (but does not save it) and sets 
        `self.field_value`.
        """
        self.field_value = value
        setattr(self.obj, self.field_name, value)
        return value

    def render_value(self, value=None):
        """Returns the field value as it should be rendered on
        the placeholder.
        """
        v = value or self.get_value()
        return apply_filters(v, self.template_filters, self.load_tags)

    def save(self):
        """Saves the object to database.

        A form is created on the fly for validation purpose, but only the 
        saved field is validated.

        **Successful save**

        >>> self.set_value('john@doe.com')
        'john@doe.com'
        >>> self.save()
        {'rendered_value': u'john@doe.com', 'error': False}

        **Validation error**
        
        >>> self.set_value('Hello world')
        'Hello world'
        >>> self.save()
        {'rendered_value': u'Hello world', 'error': True, 'value': u'Hello world',
         'messages': [{'message': u'Enter a valid e-mail address.', 'field_name': 'email_test'}]}

        """
        form = self.get_form()
        field = form[self.form_field.name]
        # We do not validate the whole form as it lead to conflicts
        if len(field.errors) == 0:
            self.obj.save()
            val = getattr(self.obj, self.field_name)
            rendered_value = self.render_value(val)
            return {
                'error': False,
                'rendered_value': self.render_value(val)}
        else:
            messages = []
            for field_name_error, errors_field in form.errors.items():
                for error in errors_field:
                    messages.append({
                        'field_name': field_name_error,
                        'message': unicode(error)
                    })
            value = self.get_value()
            return {
                'error': True,
                'messages': messages,
                'value': value,
                'rendered_value': self.render_value()}

    def render_widget(self):
        """Returns the <editlive /> HTML widget as string.

        This will also set the `self.attributes['rendered-value']`.

        >>> self.render_widget()
        <editlive app-label="myapp" field-name="firstname"
            rendered-value="John" object-id="1" data-type="charField" 
            data-field-id="id_firstname" module-name="mymodule"></editlive>

        """
        self.attributes['rendered-value'] = self.render_value()
        return u'<editlive%s></editlive>' % self.format_attributes()

    def render(self):
        """Returns the form field along with the <editlive /> tag as string

        >>> self.render()
        <input id="id_firstname" type="text" name="firstname" maxlength="25" />
        <editlive app-label="myapp" field-name="firstname"
            rendered-value="John" object-id="1" data-type="charField" 
            data-field-id="id_firstname" module-name="mymodule"></editlive>

        """
        if not self.can_edit():
            return self.render_value()
        else:
            field = unicode(self.form_field)
            if self.form_field:
                if self.kwargs.get('readonly'):
                    return self.render_value()
                if self.kwargs.get('formset'):
                    auto_id = 'id="%s"' % self.form_field.auto_id
                    name = 'name="%s"' % self.form_field.html_name
                    field = re.sub(auto_id, 'id="%s"' % self.field_id, field)
                    field = re.sub(name, 'name="%s"' % self.field_name, field)
                return mark_safe(field + self.render_widget())
            else:
                return field


class BaseInlineAdaptor(object):
    """ Experimental stuff..
    """

    def __init__(self, request, obj, manager, value, initial={}, **kwargs):
        self.request = request
        self.kwargs = kwargs['kwargs']
        self.manager_name = manager
        self.manager = getattr(obj, manager)
        self.model = self.manager.model
        self.obj = self.model()
        self.value = value
        # TODO:
        # fix this shit..
        # http://stackoverflow.com/questions/12462616/
        # finding-the-relation-field-of-a-related-object-in-django
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
            fkwargs['form'] = get_dynamic_modelform(\
                                exclude=(self.query_field, ))

        return modelform_factory(self.model, **fkwargs)

    def render(self):
        return {
            'object_list': self.get_object_list(),
            'form': self.form,
        }
