# -*- coding: utf-8 -*-

from django.db import models


class EditliveBaseFieldsTest(models.Model):
    biginteger_test = models.BigIntegerField(u'BigIntegerField test', blank=True, null=True)
    boolean_test = models.BooleanField(u'BooleanField test', default=True)
    char_test = models.CharField(u'CharField test', max_length=250, blank=True, null=True)
    commaseparatedinteger_test = models.CommaSeparatedIntegerField(max_length=250, blank=True, null=True)
    date_test = models.DateField(u'DateField test', blank=True, null=True)
    datetime_test = models.DateTimeField(u'DateTimeField test', blank=True, null=True)
    decimal_test = models.DecimalField(u'DecimalField test', decimal_places=2, max_digits=5, blank=True, null=True)
    email_test = models.EmailField(u'EmailField test', blank=True, null=True)
    file_test = models.FileField(u'FileField test', upload_to='uploads/', blank=True, null=True)
    filepath_test = models.FilePathField(u'FilePath test', blank=True, null=True)
    float_test = models.FloatField(u'FloatField test', blank=True, null=True)
    image_test = models.ImageField(u'ImageField test', upload_to='uploads/', blank=True, null=True)
    integer_test = models.IntegerField(u'IntegerField test', blank=True, null=True)
    ipaddress_test = models.IPAddressField(u'IPAdressField test', blank=True, null=True)
    genericipaddress_test = models.GenericIPAddressField(protocol='ipv4', blank=True, null=True, verbose_name=u'GenericIPAddressField test')
    nullboolean_test = models.NullBooleanField(u'NullBooleanField test', blank=True, null=True)
    positiveinteger_test = models.PositiveIntegerField(u'PositiveIntegerField test', blank=True, null=True)
    positivesmallinteger_test = models.PositiveSmallIntegerField(u'PositiveSmallIntegerField test', blank=True, null=True)
    slug_test = models.SlugField(u'SlugField test', blank=True, null=True)
    smallinteger_test = models.SmallIntegerField(u'SmallIntegerField test', blank=True, null=True)
    text_test = models.TextField(u'TextField test', blank=True, null=True)
    time_test = models.TimeField(u'TimeField test', blank=True, null=True)
    url_test = models.URLField(u'URLField test', blank=True, null=True)

