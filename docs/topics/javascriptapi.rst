The JavaScript API
++++++++++++++++++

Events
------

Editlive default widgets provides a set of events which follow the jQuery UI model.

If your custom widget subclass the charField widget like the default widgets, 
these events will also be available. Just remember to trigger them if you
override a method.

blur
====

Triggered when a field is blurred (once the placeholder is shown)

.. code-block:: javascript

    $(function(){
        $('#id_field').on('editliveblur', function(event, ui){
            var element = $(this); // Input
            var editliveInstance = ui;
            // Do something
        });
    });

change
======

Last event triggered after a succesfull save.

.. code-block:: javascript

    $(function(){
        $('#id_field').on('editlivechange', function(event, ui){
            var element = $(this); // Input
            var editliveInstance = ui;
            // Do something
        });
    });

error
=====

Triggered when a validation error occurs.

.. code-block:: javascript

    $(function(){
        $('#id_field').on('editliveerror', function(event, ui){
            var element = $(this); // Input
            var editliveInstance = ui;
            // Do something
        });
    });

focus
=====

Triggered before showing the field.

.. code-block:: javascript

    $(function(){
        $('#id_field').on('editlivefocus', function(event, ui){
            var element = $(this); // Input
            var editliveInstance = ui;
            // Do something
        });
    });

focused
=======

Triggered once the field is shown.

.. code-block:: javascript

    $(function(){
        $('#id_field').on('editlivefocus', function(event, ui){
            var element = $(this); // Input
            var editliveInstance = ui;
            // Do something
        });
    });

save
====

Triggered before saving.

.. code-block:: javascript

    $(function(){
        $('#id_field').on('editlivesave', function(event, ui){
            var element = $(this); // Input
            var editliveInstance = ui;
            // Do something
        });
    });

success
=======

Triggered after a succesfull save.

.. code-block:: javascript

    $(function(){
        $('#id_field').on('editlivesuccess', function(event, ui){
            var element = $(this); // Input
            var editliveInstance = ui;
            // Do something
        });
    });





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
