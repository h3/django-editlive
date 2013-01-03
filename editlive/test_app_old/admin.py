# -*- coding: utf-8 -*-

from django.contrib import admin
from editlive.test_app.models import EditliveBaseFieldsTest


class EditliveBaseFieldsTestAdmin(admin.ModelAdmin):
    list_display = ('char_test', 'text_test')
admin.site.register(EditliveBaseFieldsTest, EditliveBaseFieldsTestAdmin)
