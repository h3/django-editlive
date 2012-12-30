Settings
++++++++

As not editlive has only one setting which is `EDITLIVE_ADAPTORS`.

It serves as default mapping between field types and adaptors.

Currently not all field types are supported, here's the current default mapping::

    EDITLIVE_DEFAULT_ADAPTORS = {
        'char':     'editlive.adaptors.CharAdaptor',
        'text':     'editlive.adaptors.TextAdaptor',
        'date':     'editlive.adaptors.DateAdaptor',
        'datetime': 'editlive.adaptors.DateTimeAdaptor',
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
        'boolean':  'editlive.adaptors.BooleanAdaptor',
        'fk':       'editlive.adaptors.ForeignKeyAdaptor',
        'choices':  'editlive.adaptors.ChoicesAdaptor',
        'm2m':      'editlive.adaptors.ManyToManyAdaptor',
    }
