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


@after.all
def tear_down(result):
    if result.steps_failed == 0\
        and (result.features_passed == result.features_ran) \
        and (result.scenarios_passed and result.scenarios_ran):
        world.browser.quit()


def S(selector):
    return world.browser.find_element_by_css_selector(selector)


@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get('http://localhost:8000'+ url)
#   world.dom = html.fromstring(response.content)


@step(r'I see "(.*)"')
def node_exists(step, selector):
    assert S(selector)


@step(r'I see a "(.*)" editlive for "(.*)"')
def see_editlive(step, fieldtype, field_id):
    editlive = S('editlive[data-field-id="'+field_id.replace('#','')+'"]')
    assert editlive.get_attribute('data-type') == fieldtype
 

@step(r'I see "(.*)" is (hidden|visible)')
def see_html_node_visible_or_hidden(step, node_id, state):
    node = S(node_id)
    if state == 'hidden':
        assert node.is_displayed() is False
    else:
        assert node.is_displayed()
 

@step(r'I see a (hidden|visible) placeholder for "(.*)"')
def see_placeholder_visible_or_hidden(step, state, node_id):
    node = S(node_id+' + span')
    assert 'editlive' in node.get_attribute('class').split(' ')
    assert node.is_displayed()
 

@step(r'I click on the placeholder for "(.*)"')
def click_on_placeholder(step, node_id):
    node = S(node_id+' + span')
    node.click()


@step(r'I write "(.*)"')
def write(step, content):
    S(node_id).send_keys(content)
