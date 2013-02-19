# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, View
from django.template import RequestContext, Template
from django.shortcuts import render_to_response
from django.http import HttpResponse

from test_app.models import EditliveBaseFieldsTest

TEST_TEMPLATE = """
{%% extends "test_app/base.html" %%}
{%% load editlive_tags %%}
{%% block content %%}
<div class="span12">
    <h1>{{ field|capfirst }}Field</h1>
    <h3>Test: {{ options }}</h3>
    {%% editlive "object.%(fieldname)s" %(options)s as test %%}{{ test }}
</div>
{%% endblock %%}
"""

class TestView(View):
    def get(self, request, field):
        options = []
        for k in request.GET.keys():
            options.append('%s="%s"' % (k, request.GET.get(k)))

        tpl = TEST_TEMPLATE % {
            'fieldname': field + '_test',
            'options': ' '.join(options),
        }
        t = Template(tpl)
        c = RequestContext(request, {
            'field': field,
            'object': EditliveBaseFieldsTest.objects.all()[0],
        })
        return HttpResponse(t.render(c))


class TestSoupView(View):
    def get(self, request):
        return render_to_response('test_app/soup.html',{
                    'object': EditliveBaseFieldsTest.objects.all()[0]},
                    context_instance=RequestContext(request))



class HomeView(View):
    def get(self, request):
        return render_to_response('test_app/home.html',{},
                    context_instance=RequestContext(request))
