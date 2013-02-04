from django.conf.urls import patterns, url

from test_app.views import TestView, TestSoupView

urlpatterns=patterns('',
    url(r'^soup/$', TestSoupView.as_view(), name='editlive-test-soup'),
    url(r'^(?P<field>\w+)/$', TestView.as_view(), name='editlive-test'),
)
