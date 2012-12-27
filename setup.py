#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
django-editlive
"""

VERSION = __import__('editlive').VERSION

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
    'Django',
    'simplejson',
    'django-dajaxice',
]

#tests_require = [
   #'logbook',
   #'nose',
   #'unittest2',
#]

setup(
    name='editlive',
    version=VERSION,
    author='Maxime Haineault',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/django-editlive',
    description = 'Live form editing for django (prototype application',
    long_description=__doc__,
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    license='BSD',
    install_requires=install_requires,
    dependency_links=[],
   #tests_require=tests_require,
   #extras_require={'test': tests_require},
   #test_suite='nose.collector',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)



