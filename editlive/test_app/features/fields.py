from lettuce import *
from lxml import html
#from django.test.client import Client
from nose.tools import assert_equals
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
from selenium import webdriver


@before.all
def set_browser():
    world.browser = webdriver.Firefox()
#   world.browser = Client()


def S(selector):
    return world.browser.find_element_by_css_selector(selector)


@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get('http://localhost:8000'+ url)
#   world.dom = html.fromstring(response.content)


@step(r'I see a field named "(.*)" with the id "(.*)"')
def see_field(step, fieldname, field_id):
    field = S('#'+field_id)
    assert field.tag_name == 'input'
    assert field.get_attribute('type') == 'text'
    assert field.get_attribute('maxlength') == '250'
    assert field.get_attribute('name') == fieldname


@step(r'I see a editlive of type "(.*)" for the field id "(.*)"')
def see_editlive(step, fieldtype, field_id):
    editlive = S('editlive[data-field-id="'+field_id+'"]')
    assert editlive.get_attribute('data-type') == fieldtype
 

@step(r'I see the HTML node with the id "(.*)" is (hidden|visible)')
def see_html_node_visible_or_hidden(step, node_id, state):
    node = S('#'+node_id)
    if state == 'hidden':
        assert node.is_displayed() is False
    else:
        assert node.is_displayed()
 

@step(r'I see the placeholder for the id "(.*)" is (hidden|visible)')
def see_placeholder_visible_or_hidden(step, node_id, state):
    span = S('#'+node_id+' + span')
    assert 'editlive' in span.get_attribute('class').split(' ')
    assert span.is_displayed()
 

#@step(r'I click on the placeholder next to "(.*)" and see the input field appear')
#def see_placeholder(step, field_id):
#    field = world.dom.cssselect('#'+field_id)
#    assert len(field) > 0
 
 


#@step('I fill in field with class "(.*?)" with "(.*?)"')
#def fill_in_textfield_by_class(step, field_name, value):
#    with AssertContextManager(step):
#        text_field = find_field_by_class(world.browser, field_name)
#        text_field.clear()
#        text_field.send_keys(value)




#   Scenario: Placeholder test
#       Given I access the url "/editlive/test/charfield/"
#       Then I click on the placeholder next to "id_char_test" and see the input field appear

