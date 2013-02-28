# -*- coding: utf-8 -*-

VERSION = __import__('editlive').VERSION

import os
from setuptools import setup, find_packages

try:
    from setuptest import test
except ImportError:
    from setuptools.command.test import test

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = [
    'Django>=1.3,<=1.5',
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
    description = 'Live form editing for django (prototype application)',
    long_description=read('README.rst'),
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
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
    ],
)



