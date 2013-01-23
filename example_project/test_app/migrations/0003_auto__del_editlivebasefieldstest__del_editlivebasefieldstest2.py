# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EditliveBaseFieldsTest'
        db.delete_table('test_app_editlivebasefieldstest')

        # Deleting model 'EditliveBaseFieldsTest2'
        db.delete_table('test_app_editlivebasefieldstest2')


    def backwards(self, orm):
        # Adding model 'EditliveBaseFieldsTest'
        db.create_table('test_app_editlivebasefieldstest', (
            ('ipaddress_test', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('nullboolean_test', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('integer_test', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_test', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('float_test', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('smallinteger_test', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('biginteger_test', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('time_test', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('url_test', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('date_test', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('char_test', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('positiveinteger_test', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('boolean_test', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('text_test', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('commaseparatedinteger_test', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=250, null=True, blank=True)),
            ('genericipaddress_test', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('email_test', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('slug_test', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('positivesmallinteger_test', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('filepath_test', self.gf('django.db.models.fields.FilePathField')(max_length=100, null=True, blank=True)),
            ('decimal_test', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('file_test', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('test_app', ['EditliveBaseFieldsTest'])

        # Adding model 'EditliveBaseFieldsTest2'
        db.create_table('test_app_editlivebasefieldstest2', (
            ('editlivebasefieldstest_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['test_app.EditliveBaseFieldsTest'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('test_app', ['EditliveBaseFieldsTest2'])


    models = {
        
    }

    complete_apps = ['test_app']