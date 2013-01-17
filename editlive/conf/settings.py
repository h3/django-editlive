from django.conf import settings as settings


DATE_FORMAT = getattr(settings, 'DATE_FORMAT')
DATETIME_FORMAT = getattr(settings, 'DATETIME_FORMAT')

DATE_WIDGET_FORMAT = getattr(settings, 'EDITLIVE_DATE_WIDGET_FORMAT', 'yy-mm-dd')
TIME_WIDGET_FORMAT = getattr(settings, 'EDITLIVE_TIME_WIDGET_FORMAT', 'hh:mm')

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
    'time':     'editlive.adaptors.TimeAdaptor',
   #'file':     'editlive.adaptors.FileAdaptor',
   #'image':    'editlive.adaptors.ImageAdaptor',

   # Inlines
   'tabular':   'editlive.adaptors.TabularInlineAdaptor',
   'stacked':   'editlive.adaptors.StackedInlineAdaptor',
}

#EDITLIVE_SYNC_TEMPLATE = """
#<script type="text/javascript">(function($){$(function(){
#$('%(selector)s').sync({
#    model: '%(model)s',
#    app: '%(app)s',
#    property: '%(property)s'
#});
#});})(jQuery);</script>
#"""
