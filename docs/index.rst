:orphan:

.. _contents:

.. |example1| image:: /_static/examples/example-1.png
.. |example2| image:: /_static/examples/example-2.png


Django editlive documentation
=============================

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

* :ref:`genindex`
