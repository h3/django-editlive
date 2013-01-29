Creating and using custom UI widgets
++++++++++++++++++++++++++++++++++++

Extending existing widgets
==========================

Sometimes you need to use a custom widget for a field, or you simply want to
use another UI library.

Here's an example which use a dropdown menu instead of a switch button for
a boolean field:

.. code-block:: javascript

    ;(function($){

        var booleanDropDown = {
            _type: 'boolean',
            options: {
                choices: 'Yes|No'
            }
        };

        booleanDropDown._init = function() {
            var $self = this,
                label = $self.options.choices.split('|')

            $self.label_on = label[0];
            $self.label_off = label[1];
            $self.element.hide();
            $self.btn_group = $('<div class="btn-group" />').insertAfter($self.element);
            $self.btn_label = $('<button class="btn" />').appendTo($self.btn_group);
            $self.choices   = $('<ul class="dropdown-menu" />').appendTo($self.btn_group);
            $self.btn_toggle = $(['<button class="btn dropdown-toggle" data-toggle="dropdown">',
                                  '<span class="caret"></span></button>'].join(''))
                                  .insertAfter($self.btn_label);
            $self._populate();
        };

        booleanDropDown._populate = function() {
            var $self = this;
            if ($self.element.is(':checked')) {
                $('<li><a href="#off">'+ $self.label_off +'</a></li>')
                    .appendTo($self.choices)
                    .bind('click.editlive', function(){
                        $self.btn_group.removeClass('open');
                        $self.choices.find('li').remove();
                        $self.element.prop('checked', false);
                        $self.change();
                        $self._populate();
                        return false;
                    });
            }
            else {
                $('<li><a href="#on">'+ $self.label_on +'</a></li>')
                    .appendTo($self.choices)
                    .bind('click.editlive', function(){
                        $self.btn_group.removeClass('open');
                        $self.choices.find('li').remove();
                        $self.element.prop('checked', true);
                        $self.change();
                        $self._populate();
                        return false;
                    });
            }
            $self.btn_label.text(this.get_value_display());
        };

        booleanDropDown._display_errors = function(errors) {
            var $self = this;
            $.each(errors, function(k, v) {
                var el = $self.btn_group;
                el.tooltip({
                    title: v.message,
                    placement: $self.options.errorplacement
                }).tooltip('show');
            });
        };

        booleanDropDown.get_value_display = function() {
            var $self = this;
            if ($self.element.is(':checked')) {
                return $self.label_on;
            }
            else {
                return $self.label_off;
            }
        };

        booleanDropDown._get_value = function() {
            if (this.element.is(':checked')) return true;
            else return false;
        };
        
        $.widget('editliveWidgets.booleanDropDown', $.editliveWidgets.charField, booleanDropDown);

    })(jQuery);


Create a widget from scratch
============================


The JavaScript
--------------

Barebone example:

.. code-block:: javascript

    ;(function($){

        $.widget('editliveWidgets.autocompleteField', $.editliveWidgets.charField, {
            _type: 'autocomplete',
            options: {}
        });

    })(jQuery);

As is, this plugin will act exactly as a `char` field.

The charField is the base field widget, which means that looking at the source 
code of `$.editliveWidgets.charField`_ basically defines the editlive widget API.

For example, let's say we want to activate a autocomplete plugin on our field.

We'd simply override the `_create` method like this:

.. code-block:: javascript

    ;(function($){

        $.widget('editliveWidgets.autocompleteField', $.editliveWidgets.charField, {
            _type: 'autocomplete',
            options: {},

            _create: function() { 
                var $self = this;
                $.editliveWidgets.charField.prototype._create.apply(this, arguments);
                $self.element.autocomplete({minKeys: 2});
            }
        });

    })(jQuery);

For more examples please refer to the `widgets source code`_.

.. _$.editliveWidgets.charField: https://github.com/h3/django-editlive/blob/master/editlive/static/editlive/js/jquery.editlive.char.js
.. _widgets source code: https://github.com/h3/django-editlive/tree/master/editlive/static/editlive/js


The adaptor
-----------

In order to use your custom widget you will have to create a custom adaptor.

Fortunately, this is quite trivial. Here's the date picker adaptor for example:

.. code-block:: python

    class DateAdaptor(BaseAdaptor):
        """DateField adaptor"""

        def __init__(self, *args, **kwargs):
            """
            The DateAdaptor override the __init__ method
            to add the data-format argument to the 
            widget's attributes. This is what links Django internal 
            date format with the UI.
            """
            super(DateAdaptor, self).__init__(*args, **kwargs)
            field = self.form.fields.get(self.field_name)
            if field:
                self.attributes.update({'data-format': '%s' % field.widget.format})
            if self.form_field:
                self.attributes.update({'data-type': 'dateField'})

        def render_value(self, value=None):
            """
            If no custom "date" template filter is passed as argument, 
            we add one using the settings.DATE_FORMAT as value.
            """
            if self.template_filters is None:
                self.template_filters = []
            if not any(i.startswith('date:') for i in self.template_filters):
                self.template_filters.append(u"date:'%s'" % settings.DATE_FORMAT)
            return unicode(super(DateAdaptor, self).render_value(value=value))


You can browse `the adaptors source code`_ for more examples.

.. _the adaptors source code: https://github.com/h3/django-editlive/tree/master/editlive/adaptors


Using a custom adaptor
----------------------

To use a custom adaptor, simply pass a `widget` argument to editlive:

.. code-block:: django

    {% editlive "object.date_start" widget="mymodule.adaptors.MyCustomDatePickerAdaptor" as field %}
    {{ field }}

