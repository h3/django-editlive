from lettuce import world
from lettuce.django import django_url

from splinter import cookie_manager as cookie

from django.conf import settings
from django.http import HttpRequest
from django.utils.importlib import import_module
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

PAGES = {}

FIELDS = [
    'char', 'date', 'datetime', 'email', 'float', 
    'genericipaddress', 'integerfield', 'ipaddress', 
    'positiveinteger', 'positivesmallinteger', 
    'slug', 'smallinteger', 'text', 'time', 'integer']


for k in FIELDS:
    PAGES['%s' % k] = '/test/%s/' % k


@world.absorb
def go_to_page(name, querystring=''):
    assert PAGES.has_key(name), \
        'the page "%s" is not mapped in the PAGES dictionary, ' \
        'check if you misspelled it or add into it in: test_app/features/steps.py' % name
    world.browser.visit(django_url(PAGES[name]) + querystring)


@world.absorb
def is_placeholder_present(content, wait_time=10):
    return world.browser.is_element_present_by_xpath("//*[contains(concat(' ',normalize-space(@class),' '),' editlive ')][contains(text(),'"+ content +"')]", wait_time=wait_time)


@world.absorb
def is_error_present(content, wait_time=10):
    return world.browser.is_element_present_by_xpath("//*[contains(concat(' ',normalize-space(@class),' '),' tooltip-inner ')][contains(text(),'"+ content +"')]", wait_time=wait_time)


@world.absorb
def login(**credentials):
    username = credentials.get('username')
    passwd = make_password(credentials.get('password', 'test'))
    email = '%s@test.com' % username
    user, created = User.objects.get_or_create(username=username, email=email, password=passwd)
    user.is_staff = True
    user.save()

    world.browser.visit(django_url('/admin/'))
    world.browser.find_by_css('#id_username').first.fill(username)
    world.browser.find_by_css('#id_password').first.fill('test')
    world.browser.find_by_css('input[type="submit"]').first.click()


@world.absorb
def logout():
    world.browser.visit(django_url('/admin/logout/'))
