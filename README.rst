django-editlive
===============

Live form editing for django with bootstrap and jQuery UI

|BUILD|_

.. |BUILD| image:: https://api.travis-ci.org/h3/django-editlive.png?branch=master
.. _BUILD: https://travis-ci.org/h3/django-editlive/

 +-------------------+----------------+
 | **Demo page**     | To come..      |
 +-------------------+----------------+
 | **Documentation** | Read the Docs_ |
 +-------------------+----------------+
 | **Build server**  | Travis ci_     |
 +-------------------+----------------+

.. _Read the Docs: https://django-editlive.readthedocs.org/en/latest/
.. _Travis ci: https://travis-ci.org/h3/django-editlive/

Requirements
------------

 * Django-dajaxice (latest): https://github.com/jorgebastida/django-dajaxice
 * Bootstrap: http://twitter.github.com/bootstrap/
 * django-bootstrap-ui[1]: https://github.com/h3/django-bootstrap-ui


 [1] django-bootstrap-ui provides most of the JavaScript requirements, which are:

  * jQuery 1.8.2
  * jQuery ui 1.8.23 (custom build made compatible with bootstrap)
  * bootstrap 2.1.1
  * jQuery-UI-Date-Range-Picker (custom tweaks to support time inputs)

At this stage, I'm not sure yet if I will eventually ship those requirements with editlive or not.


Installation
------------

 1. Add `dajaxice` and `editlive` to your `settings.INSTALLED_APPS`
 2. Add `'dajaxice.finders.DajaxiceFinder'` to your `settings.STATICFILES_FINDERS`.
 3. Add the following code to your `settings.LOGGING['loggers']` (optional)::

     'dajaxice': {
         'handlers': ['console'],
         'level': 'WARNING',
         'propagate': False,
     },

 4. Add the Dajaxice JS to your base template::

    {% load dajaxice_templatetags %}
    {% dajaxice_js_import %}

 4. Add the editlive CSS to your base template::

    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}editlive/css/editlive.css">

 5. Add the editlive JS to your base template::

    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.js"></script>
    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.char.js"></script>
    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.text.js"></script>
    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.date.js"></script>
    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.datetime.js"></script>
    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.boolean.js"></script>
    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.foreignkey.js"></script>
    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.choices.js"></script>
    <script type="text/javascript" src="/static/editlive/js/jquery.editlive.manytomany.js"></script>

Note: not all files are required. Eventually all the JS will be minified, but meanwhile you can include just what you need.


Basic usage
-----------

Editlive can take any database object and make it editable live with a simple template tag::

    {% load editlive_tags %}

    {% editlive "object.description" as object_description %}
    <div>
        {{ object_description }}
    </div>

This will render the object's property value in a clickable container. When the container is clicked, 
it changes to a input field according to the field's type.

It is possible to apply template filters to a property value like this::

    {% editlive "object.description" template_filters="capfirst" as object_description %}

    {% editlive "object.date_visit" template_filters="date:'l j M Y at H:i\h'" as date_visit %}


The editlive tag also accept a `wrapclass` argument. If specified it will add the provided class
to the control's container.

All other argument are converted into js argument and fed to the jQuery plugin.

Working with formsets
---------------------

Formsets are a bit tricky since you need to edit multiple fields with the same id and name attributes.

So for this to work, the id and name attributes must be altered to make them unique. To achieve this,
simply pass a formset argument to editlive and give it a meaningful name::

    {% editlive "object.first_name" formset="user" as user_firstname %}
    {{ user_firstname }}

The input field will then look like this::

    <input type="text" maxlength="250" name="user_set-0-first_name" id="id_user_set-0-first_name" />


The magic
---------

To avoid conflicting with other plugins or altering the input field directly, editlive use its own
tag to bind the field properties and settings to the right input.

For example, if we were to `editlive` the `first_name` property of a user object, the output would
look something like this::

    <input type="text" maxlength="250" value="Bob" name="first_name" id="id_first_name" />
    <editlive app-label="auth" module-name="user" field-name="first_name" data-field-id="id_first_name" data-type="textField" object-id="1" rendered-value="Bob" />

This way `editlive` stays non-intrusive as it doesn't alter the original input tag.

This also means that you are not constrained to use the editlive template tag, you can create the `<editlive />` tag by hand and the JavaScript will hook it up.


More to come
------------

There is other undocumented features I will eventually document. Meanwhile you can take a look at the source code.


 * ajaxform (kind of functional, but undocummented)
 * listactions (kind of functional, but undocummented)
 * sync (experimental, not functional yet)


Credits
=======

This project was created and is sponsored by:

.. figure:: http://motion-m.ca/media/img/logo.png
    :figwidth: image

Motion Média (http://motion-m.ca)
