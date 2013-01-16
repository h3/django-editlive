from django.conf.urls import patterns, url

from test_app.views import TestView

urlpatterns=patterns('',
    url(r'^(?P<field>\w+)/$', TestView.as_view(), name='editlive-test'),
)
