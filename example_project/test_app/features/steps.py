from lettuce import *
from lettuce.django import django_url
#from lettuce_webdriver.util import assert_false
#from lettuce_webdriver.util import AssertContextManager


def S(selector, using='css', wait=0, invert=False):
    if wait > 0:
        if invert:
            method = 'is_element_present_by_%s' % using
        else:
            method = 'is_element_not_present_by_%s' % using
    else:
        method = 'find_by_%s' % using
    return getattr(world.browser, method)(selector)


def get_placeholder_for(node_id):
    n = S(node_id).first
    p = n.find_by_xpath('./ancestor::div[contains(concat(" ", @class, " "), "controls")][1]')
    return p.find_by_css('.editlive')


@step(r'I open the (\w+) test page')
def access_url(step, name):
    world.response = world.go_to_page(name)


@step(r'I open the (\w+) test page with options "(.*)"')
def access_url(step, name, options):
    world.response = world.go_to_page(name, options)


@step(u'a user exists with username "(.*)"')
def a_user_exists_with_username(step, p_username):
    user = UserProfile(username=p_username, email='example@example.com')
    user.set_password('secret007')
    user.save()


@step(r'I see "(.*)"')
def node_exists(step, selector):
    assert world.browser.is_element_present_by_css(selector)


@step(r'I see a "(.*)" editlive for "(.*)"')
def see_editlive(step, fieldtype, field_id):
    editlive = S('editlive[data-field-id="'+field_id.replace('#','')+'"]').first
    assert editlive['data-type'] == fieldtype
 

@step(r'I see "(.*)" is (hidden|visible)')
def see_html_node_visible_or_hidden(step, node_id, state):
    node = S(node_id).first
    if state == 'hidden':
        assert node.visible is False
    else:
        assert node.visible
 

@step(r'I see a (hidden|visible) placeholder for "(.*)"')
def see_placeholder_visible_or_hidden(step, state, node_id):
    node = get_placeholder_for(node_id).first
    assert 'editlive' in node['class'].split(' ')
    assert node.visible
 

@step(r'I click on the placeholder for "(.*)"')
def click_on_placeholder(step, node_id):
    node = get_placeholder_for(node_id).first
    node.click()
 

@step(r'Then the value of the placeholder for "(.*)" is "(.*)"')
def see_placeholder_visible_or_hidden(step, node_id, value):
    node = get_placeholder_for(node_id).first
    assert node.text == value


@step(r'I input "(.*)" in "(.*)"')
def write(step, content, node_id):
    n = S(node_id).first
    n.fill(content)
    assert n['value'] == content

@step(r'the value of "(.*)" is "(.*)"')
def valueof(step, node_id, value):
    n = S(node_id).first
   #import IPython
   #IPython.embed()
    assert n['value'] == value


@step(r'I input "(.*)" in "(.*)"')
def write(step, content, node_id):
    n = S(node_id).first
    n.fill(content)
    assert n['value'] == content
    world.browser.find_by_tag('h1').first.click()

@step(r'I see the placeholder text change to "(.*)"')
def write(step, content):
    assert world.is_placeholder_present(content)


@step(r'Then I see the following error: (.*)')
def errorpresent(step, error):
    assert world.is_error_present(error)
