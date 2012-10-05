# -*- coding: utf-8 -*-
import re
import collections

from django import template
from django.db import models
from django.conf import settings
from django.db.models.fields import FieldDoesNotExist
from django.db.models.fields.related import ForeignKey, ManyToManyField

from editlive.conf import settings as editlive_settings

"""
Mostly copied/inspired of: 
https://github.com/zikzakmedia/django-inplaceeditform/blob/master/inplaceeditform/commons.py
"""


def import_module(name, package=None):
    try:
        from django.utils.importlib import import_module
        return import_module(name, package)
    except ImportError:
        path = [m for m in name.split('.')]
        return __import__(name, {}, {}, path[-1])


def import_class(classpath, package=None):
    classname = classpath.split('.')[-1]
    classpath = '.'.join(classpath.split('.')[:-1])
    return getattr(import_module(classpath), classname, None)


def get_default_adaptor(field):
    if isinstance(field, str) and field == 'tabular':
        fieldtype = 'tabular'
    elif isinstance(field, str) and field == 'stacked':
        fieldtype = 'stacked'
    elif isinstance(field, models.CharField):
        fieldtype = 'text'
        if getattr(field, 'choices', None):
            fieldtype = 'choices'
    elif isinstance(field, models.TextField):
        fieldtype = 'textarea'
    elif isinstance(field, models.BooleanField):
        fieldtype = 'boolean'
    elif isinstance(field, models.DateTimeField):
        fieldtype = 'datetime'
    elif isinstance(field, models.DateField):
        fieldtype = 'date'
    elif isinstance(field, ForeignKey):
        fieldtype = 'fk'
    elif isinstance(field, ManyToManyField):
        fieldtype = 'm2m'
    elif isinstance(field, models.ImageField):
        fieldtype = 'image'
    elif isinstance(field, models.FileField):
        fieldtype = 'file'
    else:
        fieldtype = 'text'

    adaptors = getattr(settings, 'EDITLIVE_ADAPTORS', {})
    adaptors.update(editlive_settings.EDITLIVE_DEFAULT_ADAPTORS)
    adaptor = adaptors.get(fieldtype, None)

    if adaptor:
        return adaptor
    else:
       #print "Warning: %s adaptor not found" % fieldtype
        return adaptors.get('text')
    

def get_adaptor(obj, field_name, field_value=None, kwargs={}, adaptor=None):
    # Related field
    if field_name.endswith('_set'):
       #inline_type = kwargs.get('inline', 'stacked')
        if adaptor is None: adaptor = get_default_adaptor('stacked')
        path_module, class_adaptor = ('.'.join(adaptor.split('.')[:-1]), adaptor.split('.')[-1])
        Adaptor = getattr(import_module(path_module), class_adaptor)
        return Adaptor(obj, field_name, field_value, kwargs=kwargs)

    else: # Vanilla field

        if '_set-' in field_name: # Formset field
            manager, pos, field_name = filter(None, re.split(r'(\w+)_set-(\d+)-(\w+)', field_name))

        field = obj._meta.get_field_by_name(field_name)[0]
        if adaptor is None: adaptor = get_default_adaptor(field)
        path_module, class_adaptor = ('.'.join(adaptor.split('.')[:-1]), adaptor.split('.')[-1])
        Adaptor = getattr(import_module(path_module), class_adaptor)

        return Adaptor(field, obj, field_name, field_value=field_value, kwargs=kwargs)


def get_dict_from_obj(obj):
    obj_dict = obj.__dict__
    obj_dict_result = obj_dict.copy()
    for key, value in obj_dict.items():
        if '_id' in key:
            key2 = key.replace('_id', '')
            obj_dict_result[key2] = obj_dict_result[key]
            del obj_dict_result[key]
    manytomany_list = obj._meta.many_to_many
    for manytomany in manytomany_list:
        val = manytomany.value_from_object(obj)
        if isinstance(val, collections.Iterable):
            ids = [obj_rel.id for obj_rel in val]
            if ids:
                obj_dict_result[manytomany.name] = ids

    return obj_dict_result


def apply_filters(value, filters, load_tags=None):
    if filters:
        filters_str = '|%s' % '|'.join(filters)
        load_tags = load_tags or []
        if load_tags:
            load_tags_str = "{%% load %s %%}" % ' '.join(load_tags)
        else:
            load_tags_str = ""
        value = template.Template("""%s{{ value%s }}""" % (load_tags_str, filters_str)).render(template.Context({'value': value}))
    return value
