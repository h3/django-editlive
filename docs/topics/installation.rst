Installation
++++++++++++

First you will need to install `Dajaxice`_. If you use pip or buildout, simply add it to your requirements and rebuild your environment.

.. _Dajaxice: http://www.dajaxproject.com/#dajaxice

Then add `dajaxice.finders.DajaxiceFinder` to your `settings.STATICFILES_FINDERS`.

Add the Dajaxice JS to your base template::

    {%load dajaxice_templatetags%}
    {%dajaxice_js_import%}

Add the editlive CSS and JS to your base template:

.. code-block:: django

    {% load dajaxice_templatetags %}
    {# jQuery + jQuery UI + Bootstrap #}
    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}editlive/contrib/jquery-ui-bootstrap/css/style.css">
    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}editlive/contrib/bootstrap/css/bootstrap-responsive.min.css">
    <script type="text/javascript" src="{{ STATIC_URL }}editlive/contrib/jquery-ui-bootstrap/js/jquery.min.js"></script>
    <script type="text/javascript" src="{{ STATIC_URL }}editlive/contrib/jquery-ui-bootstrap/js/jquery-ui.custom.min.js"></script>
    <script type="text/javascript" src="{{ STATIC_URL }}editlive/contrib/jquery-ui-bootstrap/js/bootstrap/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}editlive/contrib/jquery-ui-bootstrap/third-party/jQuery-UI-Date-Time-Picker/jquery-ui-timepicker.css">
    <script type="text/javascript" src="{{ STATIC_URL }}editlive/contrib/jquery-ui-bootstrap/third-party/jQuery-UI-Date-Time-Picker/jquery-ui-timepicker-addon.js"></script>
    <script type="text/javascript" src="{{ STATIC_URL }}editlive/contrib/bootstrap/js/bootstrap.min.js"></script>
    {% dajaxice_js_import %}
    {# Editlive #}
    <link rel="stylesheet" type="text/css" href="{{STATIC_URL}}editlive/css/editlive.css">
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.js"></script>
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.char.js"></script>
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.text.js"></script>
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.date.js"></script>
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.datetime.js"></script>
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.boolean.js"></script>
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.foreignkey.js"></script>
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.choices.js"></script>
    <script src="{{STATIC_URL}}editlive/js/jquery.editlive.manytomany.js"></script>


**Note:** not all files are required. Eventually all the JS will be minified. Meanwhile you can include what you need or use something like django-pipeline.

**Protip:** You can add the following logger to your settings.LOGGING['loggers'] to redirect dajaxice exceptions to the console.
::
    'dajaxice': {
        'handlers': ['console'],
        'level': 'WARNING',
        'propagate': False,
    },
