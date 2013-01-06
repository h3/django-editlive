from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from dajaxice.core import dajaxice_autodiscover

from test_app.views import HomeView

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^dajaxice/', include('dajaxice.urls')),
    url(r'^test/', include('test_app.urls')),
    # This is just to avoid a 404 in the test runner .. whatever.
    url(r'^$', HomeView.as_view(), name='editlive-home'),
#   url(r'^admin/', include(admin.site.urls)),
    (r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {
        'url': '%stest_app/img/favicon.ico' % settings.STATIC_URL}),
)

if settings.DEV:
    urlpatterns += patterns('', 
        (r'^%s(.*)$' % settings.MEDIA_URL[1:], 
        'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        
    )

