"""
TODO: move to a register system instead, which will allow more complex adaptor schemes

ex:

import editlive

class TextAdaptorOption(AdaptorOption):
    auto_fields = ['django.db.models.CharField']
    is_active(self, field):
        return not getattr(field, 'choices')
editlive.register(TextAdaptorOption)


class TextChoicesAdaptorOption(TextAdaptorOption):
    get_auto_field(self):
        fields = self.auto_fields
        fields.append('custom.models.CharField')
        return fields

    is_active(self, field):
        return getattr(field, 'choices')
editlive.register(TextChoicesAdaptorOption)


"""

EDITLIVE_DEFAULT_ADAPTORS = {
    # Fields
    'char':     'editlive.adaptors.CharAdaptor',
    'text':     'editlive.adaptors.TextAdaptor',
    'date':     'editlive.adaptors.DateAdaptor',
    'datetime': 'editlive.adaptors.DateTimeAdaptor',
    'boolean':  'editlive.adaptors.BooleanAdaptor',
    'fk':       'editlive.adaptors.ForeignKeyAdaptor',
    'choices':  'editlive.adaptors.ChoicesAdaptor',
    'm2m':      'editlive.adaptors.ManyToManyAdaptor',
   #'textarea': 'editlive.adaptors.TextAreaAdaptor',
   #'file':     'editlive.adaptors.FileAdaptor',
   #'image':    'editlive.adaptors.ImageAdaptor',

   # Inlines
   'tabular':   'editlive.adaptors.TabularInlineAdaptor',
   'stacked':   'editlive.adaptors.StackedInlineAdaptor',
}

