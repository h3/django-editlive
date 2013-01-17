Settings
++++++++


EDITLIVE_DATE_WIDGET_FORMAT
---------------------------

This setting is used to pass the date format to the datepicker widget.

The format used must match one of the format of the django setting `DATE_INPUT_FORMAT` 
which itself is used by django to parse and validate input content.

By default `DATE_INPUT_FORMAT` is set to the following::

    ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d',
    '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M', '%m/%d/%Y',
    '%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M', '%m/%d/%y')

Here's a translation table for Python / Django / jQuery UI date format:

+----+----+----+---------------------------------------+
| Py | Dj | Js | Description                           |
+====+====+====+=======================================+
|    | j  | d  | day of month (no leading zero)        |
+----+----+----+---------------------------------------+
| d  | d  | dd | day of month (two digit)              |
+----+----+----+---------------------------------------+
|    | z  | o  | day of the year (no leading zeros)    |
+----+----+----+---------------------------------------+
| j  | z  | oo | day of the year (three digit) *       |
+----+----+----+---------------------------------------+
| a  | D  | D  | day name short                        |
+----+----+----+---------------------------------------+
| A  | l  | DD | day name long                         |
+----+----+----+---------------------------------------+
|    | n  | m  | month of year (no leading zero)       |
+----+----+----+---------------------------------------+
| m  | m  | mm | month of year (two digit)             |
+----+----+----+---------------------------------------+
| b  | M  | M  | month name short                      |
+----+----+----+---------------------------------------+
| B  | F  | MM | month name long                       |
+----+----+----+---------------------------------------+
| y  | y  | y  | year (two digit)                      |
+----+----+----+---------------------------------------+
| Y  | Y  | yy | year (four digit)                     |
+----+----+----+---------------------------------------+
|    | U  | @  | Unix timestamp (ms since 01/01/1970)  |
+----+----+----+---------------------------------------+

As you can see .. this is quite a mess:

 * Django use the setting `DATE_FORMAT` to render dates in template. 
   It has its own date formatting implementation described in the builtin
   `date template filter documentation`_.

 * Then to parse and validate date inputs it uses the `DATE_INPUT_FORMAT` which
   uses the `Python strptime format`_

 * And finally, the `DATE_WIDGET_FORMAT` is used by editlive to set the datepicker
   format, which must validate against a `DATE_INPUT_FORMAT`. The `DATE_WIDGET_FORMAT`
   use the jQuery UI date format as described in the `datepicker documentation`_.

At this point you might want to take a little time for yourself and cry a little bit. 
   
.. _date template filter documentation: https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
.. _Python strptime format: http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
.. _datepicker documentation: http://docs.jquery.com/UI/Datepicker/formatDate


EDITLIVE_TIME_WIDGET_FORMAT
--------------------------

This setting is used to pass the time format to the timepicker plugin.

In Django the datetime format is specified as a single argument (for example: `%Y-%m-%d %H:%M:%S`).

But jQuery UI uses two seperate settings for the date and time formats.

Here's the translation table for the time formatting:

+----+----+----+---------------------------------------+
| Py | Dj | Js | Description                           |
+====+====+====+=======================================+
| H  | h-H| hh | Hour, 12/24-hour format.              |
+----+----+----+---------------------------------------+
|    | g  | h  | Hour, 12/24-hour format without zeros |
+----+----+----+---------------------------------------+
| M  | i  | mi | Minutes with zeros.                   |
+----+----+----+---------------------------------------+
|    |    | m  | Minutes (unsupported by django)       |
+----+----+----+---------------------------------------+
| S  | s  | ss | Seconds, 2 digits with leading zeros  |
+----+----+----+---------------------------------------+
|    |    | s  | Seconds (unsupported by django)       |
+----+----+----+---------------------------------------+
| f  | u  | l  | Microseconds                          |
+----+----+----+---------------------------------------+
| Z  | T  | z  | Time zone                             |
+----+----+----+---------------------------------------+
|    |    | t  | AM/PM (unsupported by django)         |
+----+----+----+---------------------------------------+
| P  | A  | tt | AM/PM                                 |
+----+----+----+---------------------------------------+

You can find the full `timepicker formatting reference here`_.

.. _timepicker formatting reference here: http://trentrichardson.com/examples/timepicker/#tp-formatting


EDITLIVE_ADAPTORS
-----------------

This setting serves as default mapping between field types and adaptors.

Currently not all field types are supported, here's the current default mapping::

    EDITLIVE_DEFAULT_ADAPTORS = {
        'char':     'editlive.adaptors.CharAdaptor',
        'text':     'editlive.adaptors.TextAdaptor',
        'date':     'editlive.adaptors.DateAdaptor',
        'datetime': 'editlive.adaptors.DateTimeAdaptor',
        'time':     'editlive.adaptors.TimeAdaptor',
        'boolean':  'editlive.adaptors.BooleanAdaptor',
        'fk':       'editlive.adaptors.ForeignKeyAdaptor',
        'choices':  'editlive.adaptors.ChoicesAdaptor',
        'm2m':      'editlive.adaptors.ManyToManyAdaptor',
    }


If you want to override the datetime adaptor with your own, you can 
simply provide one in your `settings.py` like so::


    EDITLIVE_ADAPTORS = {
        'datetime': 'mymodule.adaptors.MyDateTimeAdaptor',
    }

The settings `EDITLIVE_ADAPTORS` updates the adaptor mapping instead of 
overwriting it, so the end result would be this::


    EDITLIVE_DEFAULT_ADAPTORS = {
        'char':     'editlive.adaptors.CharAdaptor',
        'text':     'editlive.adaptors.TextAdaptor',
        'date':     'editlive.adaptors.DateAdaptor',
        'datetime': 'mymodule.adaptors.MyDateTimeAdaptor',
        'time':     'editlive.adaptors.TimeAdaptor',
        'boolean':  'editlive.adaptors.BooleanAdaptor',
        'fk':       'editlive.adaptors.ForeignKeyAdaptor',
        'choices':  'editlive.adaptors.ChoicesAdaptor',
        'm2m':      'editlive.adaptors.ManyToManyAdaptor',
    }
