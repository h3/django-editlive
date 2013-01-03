# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from editlive.test_app.models import EditliveBaseFieldsTest

FIELD_TYPES = [
    {'field':'object.biginteger_test','label':'BigIntegerField'},
    {'field':'object.boolean_test','label':'BooleanField', 'include': 'website/fields/boolean.inc.html'},
    {'field':'object.char_test','label':'CharField'},
    {'field':'object.commaseparatedinteger_test','label':'CommaSeparatedIntegerField'},
    {'field':'object.date_test','label':'DateField'},
   #{'field':'object.datetime_test','label':'DateTimeField'},
    {'field':'object.decimal_test','label':'DecimalField'},
    {'field':'object.email_test','label':'EmailField'},
   #{'field':'object.file_test','label':'FileField'},
    {'field':'object.filepath_test','label':'FilePathField'},
    {'field':'object.float_test','label':'FloatField'},
   #{'field':'object.image_test','label':'ImageField'},
    {'field':'object.integer_test','label':'IntegerField'},
    {'field':'object.ipaddress_test','label':'IPAddressField'},
    {'field':'object.genericipaddress_test','label':'GenericIPAddressField'},
   #{'field':'object.nullboolean_test','label':'NullBooleanField'},
    {'field':'object.positiveinteger_test','label':'PositiveIntegerField'},
    {'field':'object.positivesmallinteger_test','label':'PositiveSmallIntegerField'},
    {'field':'object.slug_test','label':'SlugField'},
    {'field':'object.smallinteger_test','label':'SmallIntegerField'},
    {'field':'object.text_test','label':'TextField'},
    {'field':'object.time_test','label':'TimeField'},
    {'field':'object.url_test','label':'URLField'},
]


class TestView(TemplateView):
    def get_template_names(self):
        return ["editlive/test/%s.html" % self.kwargs.get('name')]

    def get_context_data(self, *args, **kwargs):
        context = super(TestView, self).get_context_data(*args, **kwargs)
        context['field_types'] = FIELD_TYPES
        try:
            context['object'] = EditliveBaseFieldsTest.objects.all()[0]
        except:
            pass
        return context

