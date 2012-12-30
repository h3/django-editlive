# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from editlive.test_app.views import *

urlpatterns=patterns('',
    url(r'^test/(?P<name>\w+)/$', TestView.as_view(), name='editlive-test'),
)

