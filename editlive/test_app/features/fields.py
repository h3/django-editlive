from lettuce import *
from lettuce.django import django_url
from nose.tools import assert_equals
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager


def S(selector):
    return world.browser.find_by_css(selector)[0]


def get_placeholder_for(node_id):
    n = S(node_id)
    p = n.find_by_xpath('./ancestor::div[contains(concat(" ", @class, " "), "controls")][1]')
    return S('.editlive')


@step(r'I access the url "(.*)"')
def access_url(step, url):
    world.response = world.browser.visit(django_url(url))


@step(u'I should see "(.*)"')
def i_should_see(step, text):
    assert text in world.browser.html

@step(u'a user exists with username "(.*)"')
def a_user_exists_with_username(step, p_username):
    user = UserProfile(username=p_username, email='example@example.com')
    user.set_password('secret007')
    user.save()


@step(r'I see "(.*)"')
def node_exists(step, selector):
    assert S(selector)


@step(r'I see a "(.*)" editlive for "(.*)"')
def see_editlive(step, fieldtype, field_id):
    editlive = S('editlive[data-field-id="'+field_id.replace('#','')+'"]')
    assert editlive['data-type'] == fieldtype
 

@step(r'I see "(.*)" is (hidden|visible)')
def see_html_node_visible_or_hidden(step, node_id, state):
    node = S(node_id)
    if state == 'hidden':
        assert node.visible is False
    else:
        assert node.visible
 

@step(r'I see a (hidden|visible) placeholder for "(.*)"')
def see_placeholder_visible_or_hidden(step, state, node_id):
    node = get_placeholder_for(node_id)
    assert 'editlive' in node['class'].split(' ')
    assert node.visible
 

@step(r'I click on the placeholder for "(.*)"')
def click_on_placeholder(step, node_id):
    node = get_placeholder_for(node_id)
    node.click()


@step(r'I input "(.*)" in "(.*)"')
def write(step, content, node_id):
    S(node_id).fill(content)


@step(r'the value of "(.*)" is "(.*)"')
def valueof(step, node_id, value):
    assert S(node_id)['value'] == value
