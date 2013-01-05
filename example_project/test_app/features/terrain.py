from lettuce import world
from lettuce.django import django_url

PAGES = {}

FIELDS = [
    'char', 'date', 'datetime', 'email', 'float', 
    'genericipaddress', 'integerfield', 'ipaddress', 
    'positiveinteger', 'positivesmallinteger', 
    'slug', 'smallinteger', 'text', 'time', 'integer']


for k in FIELDS:
    PAGES['%s' % k] = '/test/%s/' % k


@world.absorb
def go_to_page(name):
    assert PAGES.has_key(name), \
        'the page "%s" is not mapped in the PAGES dictionary, ' \
        'check if you misspelled it or add into it in: test_app/features/steps.py' % name
    world.browser.visit(django_url(PAGES[name]))

@world.absorb
def is_placeholder_present(content, wait_time=10):
    return world.browser.is_element_present_by_xpath("//*[contains(concat(' ',normalize-space(@class),' '),' editlive ')][contains(text(),'"+ content +"')]", wait_time=wait_time)

@world.absorb
def is_error_present(content, wait_time=10):
    return world.browser.is_element_present_by_xpath("//*[contains(concat(' ',normalize-space(@class),' '),' tooltip-inner ')][contains(text(),'"+ content +"')]", wait_time=wait_time)
