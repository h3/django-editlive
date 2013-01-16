Creating and using custom UI widgets
++++++++++++++++++++++++++++++++++++


The JavaScript
--------------

Barebone example::

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

We'd simply override the `_create` method like this::

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

Fortunately, this is quite trivial. Here's the date picker adaptor for example::


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
-----------

To use a custom adaptor, simply pass a `widget` argument to editlive::


    {% editlive "object.date_start" widget="mymodule.adaptors.MyCustomDatePickerAdaptor" as field %}
    {{ field }}

