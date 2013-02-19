django-editlive
===============

Live form editing for django with Bootstrap_ and `jQuery UI`_

 +-------------------+-----------------------------+
 | **Demo page**     | To come..                   |
 +-------------------+-----------------------------+
 | **Documentation** | `Read the Docs`_            |
 +-------------------+-----------------------------+
 | **Build server**  | `Travis ci`_ |BUILDSTATUS|_ |
 +-------------------+-----------------------------+

.. _Bootstrap: http://twitter.github.com/bootstrap/index.html
.. _jQuery UI: http://jqueryui.com/
.. |BUILDSTATUS| image:: https://api.travis-ci.org/h3/django-editlive.png?branch=master
.. _BUILDSTATUS: https://travis-ci.org/h3/django-editlive/
.. _Read the Docs: https://django-editlive.readthedocs.org/en/latest/
.. _Travis ci: https://travis-ci.org/h3/django-editlive/


Requirements
------------

* `Django-dajaxice`_ (latest)

.. _Django-dajaxice: https://github.com/jorgebastida/django-dajaxice

Basic usage
-----------

In a template, editlive can take any in context database object and make it editable live with a simple template tag:

.. code-block:: django

    {% load editlive_tags %}

    {% editlive "object.description" as object_description %}
    <div>
        {{ object_description }}
    </div>

This will render the object's property value in a clickable container. When the container is clicked, 
it changes to a input field according to the field's type.

It's possible to apply template filters to the placeholder's display value like this:

.. code-block:: django

    {% editlive "object.description" template_filters="capfirst" as object_description %}

    {% editlive "object.date_visit" template_filters="date:'l j M Y at H:i\h'" as date_visit %}

Most other arguments are converted into js options and fed to the jQuery UI widget.

Working with formsets
---------------------

Formsets are a bit tricky since you need to edit multiple fields with the same id and name attributes.

So for this to work, the id and name attributes must be altered to make them unique. To achieve this,
simply pass a formset argument to editlive and give it a meaningful name:

.. code-block:: django

    {% editlive "object.first_name" formset="user" as user_firstname %}
    {{ user_firstname }}

The input field will then look like this:

.. code-block:: html

    <input type="text" maxlength="250" name="user_set-0-first_name" id="id_user_set-0-first_name" />


The magic
---------

To avoid conflicting with other plugins or altering the input field directly, editlive use its own
tag to bind the field properties and settings to the right input.

For example, if we were to `editlive` the `first_name` property of a user object, the output would
look something like this:

.. code-block:: html

    <input type="text" maxlength="250" value="Bob" name="first_name" id="id_first_name" />
    <editlive app-label="auth" module-name="user" field-name="first_name" data-field-id="id_first_name" data-type="textField" object-id="1" rendered-value="Bob" />

This way `editlive` stays non-intrusive as it doesn't alter the original input tag.

This also means that you are not constrained to use the editlive template tag, you can hardcode `<editlive />` tag in HTML and the JavaScript will hook it up.


Credits
=======

This project was created and is sponsored by:

.. figure:: http://motion-m.ca/media/img/logo.png
    :figwidth: image

Motion Média (http://motion-m.ca)
