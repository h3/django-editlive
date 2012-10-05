# -*- coding: utf-8 -*-

from django import template
from django.template import Variable
#from django.conf import settings

from editlive.utils import get_adaptor

register = template.Library()

@register.assignment_tag(takes_context=True)
def editlive(context, context_variable, **kwargs):
    field_value = Variable(context_variable).resolve(context)
    field_name  = context_variable.split('.')[-1]
    adaptor_str = kwargs.get('adaptor', None) # Ex: "editlive.adaptors.TextAdaptor"
    context_obj = Variable(context_variable.split('.')[0]).resolve(context)
    
    if kwargs.get('formset'):
        try:
            kwargs['field-index'] = Variable('forloop.counter0').resolve(context)
        except:
            kwargs['field-index'] = 0

    adaptor = get_adaptor(context_obj, field_name, field_value=field_value, kwargs=kwargs, adaptor=adaptor_str)
    return adaptor.render()
