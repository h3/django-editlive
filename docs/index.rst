.. _index:

.. _contents:

.. |example1| image:: /_static/example-1.png
.. |example2| image:: /_static/example-2.png

=============================
Django editlive documentation
=============================

.. rubric:: Everything you need to know about Django editlive.

.. sidebar:: Live examples

    You can `see editlive in action on here`__

.. __: http://editlive.motion-m.ca/


Django editlive is a Free Open Source project which aims to make it easy to
make elegant inline editable fields from database objects.

Here's a simple example::

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

Topics
======

Adaptors are special classes which are used to abstract the different fields types and 
interact with them. Learn more about it below:

* :ref:`genindex`

* **General:**

  * :doc:`Installation <topics/installation>`
  * :doc:`Settings <topics/settings>`
  * :doc:`Utils <topics/utils>`
  * :doc:`JavaScript API <topics/javascriptapi>`

* **Adaptors:**

  * :doc:`BaseAdaptor <topics/adaptors/base>`
  * :doc:`BooleanAdaptor <topics/adaptors/boolean>`
  * :doc:`CharAdaptor <topics/adaptors/char>`
  * :doc:`ChoicesAdaptor <topics/adaptors/choices>`
  * :doc:`DateAdaptor and DateTimeAdaptor <topics/adaptors/date>`
  * :doc:`ForeignKeyAdaptor <topics/adaptors/foreignkey>`
  * :doc:`ManyToManyAdaptor <topics/adaptors/manytomany>`
  * :doc:`TextAdaptor <topics/adaptors/text>`

* **UI Widgets:**

  * :doc:`booleanField <topics/widgets/boolean>`
  * :doc:`charField <topics/widgets/char>`
  * :doc:`choicesField <topics/widgets/choices>`
  * :doc:`dateField <topics/widgets/date>`
  * :doc:`datetimeField <topics/widgets/datetime>`
  * :doc:`foreignkeyField <topics/widgets/foreignkey>`
  * :doc:`manytomanyField <topics/widgets/manytomany>`
  * :doc:`textField <topics/widgets/text>`
  * :doc:`Writing custom widgets <topics/widgets/custom>`
