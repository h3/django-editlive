# -*- coding: utf-8 -*-

from django.conf import settings

if 'django.contrib.admin' in settings.INSTALLED_APPS:

    from django.contrib import admin
    from test_app.models import EditliveBaseFieldsTest


    class EditliveBaseFieldsTestAdmin(admin.ModelAdmin):
        list_display = ('char_test', 'text_test')
    admin.site.register(EditliveBaseFieldsTest, EditliveBaseFieldsTestAdmin)
