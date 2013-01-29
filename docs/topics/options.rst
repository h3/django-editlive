Options
+++++++

The editlive template tags accepts three kind of options.

 * **template tag options**: these options affect the template tag behavior
 * **data options**: options starting with `data_` 
 * **widget options**: all other options you may pass will be sent to the jQuery UI widget

Template tag options
--------------------

wrapclass
^^^^^^^^^

Add a CSS class to the control's container.:

.. code-block:: django

    {%load editlive_tags%}
    {%editlive "object.date_test" wrapclass="lead" as field%}{{field}}

load_tags
^^^^^^^^^

Editlive fields are rendered with standard django template. This option is used to load extra 
template tags in these template instance. As is this option is not really useful, it's more a 
complement to the next option.

template_filters
^^^^^^^^^^^^^^^^

With the `template_filters` option you can control the rendering of the placeholder value.
