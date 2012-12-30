from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I see a field named "(.*)" with the id "(.*)"')
def see_field(step, fieldname, field_id):
    field = world.dom.cssselect('#'+ field_id)
    assert len(field) > 0 and field[0].attrib['name'] == fieldname 


@step(r'Then I see a editlive of type "(.*)" with the field id "(.*)"')
def see_editlive(step, fieldtype, field_id):
    editlive = world.dom.cssselect('editlive[data-field-id="'+field_id+'"]')
    assert len(editlive) > 0 and editlive[0].attrib['data-type'] == fieldtype


@step(r'I click on the placeholder next to "(.*)" and see the input field appear')
def see_placeholder(step, field_id):
    field = world.dom.cssselect('#'+field_id)
    import IPython
    IPython.embed()
    assert len(editlive) > 0 and editlive[0].attrib['data-type'] == fieldtype
