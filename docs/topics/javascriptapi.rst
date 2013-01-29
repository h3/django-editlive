The JavaScript API
++++++++++++++++++


$.fn.editlive
-------------

This is a gateway function used to interact with an instancied editlive field.


val
^^^

Val is used to get and set the field value:

.. code-block:: javascript

    $('#id_char_test').editlive('val');
    "Hello World"

    $('#id_char_test').editlive('val', 'Hello Universe');
    "Hello Universe"


$.editlive.load
---------------

Scan the entire document for editlive tags and load their widgets:

.. code-block:: javascript

    $(function(){
        $.editlive.load();
    });

This is equivalent of doing this:

.. code-block:: javascript

    $(function(){
        $('editlive').each(function(k, v) {
            $.editlive.loadWidget(v);
        });
    });

You can also pass a selector as parent:

.. code-block:: javascript

    $(function(){
        $.editlive.load('#my-ajax-content-wrapper');
    });


$.editlive.loadWidget
---------------------

Load a given editlive widget element:

.. code-block:: javascript
    
    $(function(){
        var widget = $('editlive:first');
        $.editlive.loadWidget(widget);
    });
