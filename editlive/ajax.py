from django.utils import simplejson
from django.db.models import get_model
from django.shortcuts import get_object_or_404
from django.forms.models import modelform_factory

from dajaxice.decorators import dajaxice_register

from editlive.utils import get_adaptor, import_class


@dajaxice_register(method='POST')
def save(request, **kwargs):
    field_name    = kwargs.get('field_name')
    field_value   = kwargs.get('field_value')
    object_id     = kwargs.get('object_id')
    app_label     = kwargs.get('app_label')
    module_name   = kwargs.get('module_name')
    field_options = kwargs.get('field_options')
    Model         = get_model(app_label, module_name)
    obj           = get_object_or_404(Model, pk=object_id)
    adaptor       = get_adaptor(obj, field_name)
    tpl_filters   = kwargs.get('tpl_filters')

    if tpl_filters: adaptor.template_filters = tpl_filters.split('|')
    adaptor.set_value(field_value)

    return simplejson.dumps(adaptor.save())


@dajaxice_register(method='POST')
def save_form(request, **kwargs):
    meta  = kwargs.get('meta')
    model = get_model(*meta.get('model').split('.'))
    fkwargs = {}

    if meta.get('formClass'):
        form_class = import_class(meta.get('formClass'))
    else:
        form_class = modelform_factory(model)

    if meta.get('formPrefix'):
        fkwargs['prefix'] = meta.get('formPrefix')

    form = form_class(kwargs.get('data'), **fkwargs)

    if form.is_valid():
        form.save()
        out = { 'error': False }
    else: 
        messages = []
        for field_name_error, errors_field in form.errors.items():
            for error in errors_field:
                messages.append({'field_name': field_name_error, 'message': unicode(error)})

        out = {'error': True, 'messages': messages}

    return simplejson.dumps(out)


@dajaxice_register(method='POST')
def delete_objects(request, **kwargs):
    # Todo: permission & app/model whitelist
    object_list   = kwargs['objects']
    app_label     = kwargs['meta'].get('appLabel')
    module_name   = kwargs['meta'].get('moduleName')
    Model         = get_model(app_label, module_name)
    out = {
        'error': False, 
        'object_list': object_list,
        'app_label': kwargs['meta'].get('appLabel'),
        'module_name': kwargs['meta'].get('moduleName'),
    }
    try:
        Model.objects.filter(pk__in=object_list).delete()
    except:
        out['error'] = True
        out['message'] = 'Erreur lors de la suppression des objets'

    return simplejson.dumps(out)

import re
from editlive.utils import get_field_type

@dajaxice_register(method='POST')
def sync(request, **kwargs):
    # On the first pass we collect data from the database
    # while trying to limit queries as much as possible
    rs = {}
    for model in kwargs:
        ids = list(set([x['object_id'] for x in kwargs[model]]))
        rs[model] = get_model(*model.split('.')).objects.filter(pk__in=ids)

    # Then we correlate the data and send back only what
    # has changed
    for model in kwargs:
        for field in kwargs[model]:
            obj = rs[model].get(pk=field['object_id'])
            if '_set-' in field['field_name']: # Fieldset
                field_name = re.sub(r"\w+_set-\d+-", '', field['field_name'])
            else: # Normal field
                field_name = field['field_name']

            adaptor = get_adaptor(obj, field_name)
            oldval = field.get('value', 'None')
            newval = adaptor.get_value()

            if unicode(oldval) != unicode(newval):
                print unicode(newval) == unicode('None')
                print "%s!=%s (CHANGED)" % (oldval, newval)
           #else:
           #    print "%s==%s" % (oldval, newval)
            
    return simplejson.dumps({})
