.. almir documentation master file, created by

.. _index:
.. _contents:

.. |example1| image:: /_static/example-1.png
.. |example2| image:: /_static/example-2.png

Django editlive documentation
+++++++++++++++++++++++++++++


:Author: Maxime Haineault <max@motion-m.ca>
:Source code: `github.com project <https://github.com/h3/django-editlive/>`_
:Bug tracker: `github.com issues <https://github.com/h3/django-editlive/issues>`_
:Generated: |today|
:License: Open source, `BSD license`_
:Version: |release|

.. _BSD license: https://github.com/h3/django-editlive/blob/master/LICENSE

.. rubric:: Everything you need to know about Django editlive.

.. sidebar:: Live examples

    You can `see editlive in action on here`__

.. __: http://editlive.motion-m.ca/


Django editlive is a Free Open Source project which aims to make it easy to
make elegant inline editable fields from database objects.

Here's a simple example:

.. code-block:: django

    {% load editlive_tags %}

    {% editlive "request.user.first_name" as firstname %}
    Hello {{ firstname }}, how are you ?


This would output something like `Hello [John], how are you ?`.

|example1|

The name `[John]` would be a clickable `span` element called the "placeholder".

|example2|

When the placeholder is clicked, it's replaced by an input field and when this field
is blurred, it is automatically saved to the database with AJAX. To cancel an edit you
must use the escape key.


Adaptors are special classes which are used to abstract the different fields types and 
interact with them. Learn more about it below:

Table of Contents
=================

.. toctree::
   :maxdepth: 2

   topics/installation
   topics/settings
   topics/usage-examples
   topics/options
   topics/javascriptapi
   topics/adaptors
   topics/widgets
   topics/developers
