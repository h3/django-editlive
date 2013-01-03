from django.conf.urls import patterns, url

from test_app.views import *

urlpatterns=patterns('',
    url(r'^(?P<name>\w+)/$', TestView.as_view(), name='editlive-test'),
)

