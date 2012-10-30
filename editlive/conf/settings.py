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
