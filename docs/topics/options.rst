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

mini
^^^^

Smaller placeholder/input.

maxwidth
^^^^^^^^

Set max width of the placeholder.

width
^^^^^

Set the width of the placeholder.

readonly
^^^^^^^^

Toggle readonly mode:

.. code-block:: django

    {%load editlive_tags%}
    {%editlive "object.date_test" readonly=object.is_archived as field%}{{field}}

formset
^^^^^^^

If you are iterating over a object set you will need to use the formset argument so
each field as its own id.

.. code-block:: django

    <table>
        {% for line in object.relatedobject_set.all %}
        <tr>
            <td>{% editlive "line.name" formset="myformset" line_name %}{{ line_name }}</td>
            <td>{% editlive "line.email" formset="myformset" line_email %}{{ line_email }}</td>
        </tr>
        {% endfor %}
    </table>

class
^^^^^

Add class to the wrapper. A `fixedwidth` class helper is provided. When used in conjunction with
`width`, if the text of the placeholder is wider than its container will be truncated and an elipsis
will be added:

class="fixedwidth span1"

.. code-block:: django

    {%load editlive_tags%}
    {%editlive "object.date_test" width="100" class="fixedwidth" as field%}{{field}}
