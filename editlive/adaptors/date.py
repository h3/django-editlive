from django.conf import settings
from editlive.adaptors.base import BaseAdaptor


class DateAdaptor(BaseAdaptor):
    """DateField adaptor
    """
    def __init__(self, *args, **kwargs):
        super(DateAdaptor, self).__init__(*args, **kwargs)
        field = self.form.fields.get(self.field_name)
        if field:
            self.attributes.update({'data-format': '%s' % field.widget.format})
        if self.form_field:
            self.attributes.update({'data-type': 'dateField'})

    def render_value(self, value=None):
        if self.template_filters is None:
            self.template_filters = []
        if not any(i.startswith('date:') for i in self.template_filters):
            self.template_filters.append(u"date:'%s'" % settings.DATE_FORMAT)
        return unicode(super(DateAdaptor, self).render_value(value=value))


class DateTimeAdaptor(BaseAdaptor):
    """ DateTimeField adaptor
    """
    def __init__(self, *args, **kwargs):
        super(DateTimeAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'datetimeField'})

    def render_value(self, value=None):
        if self.template_filters is None:
            self.template_filters = []
        if not any(i.startswith('date:') for i in self.template_filters):
            self.template_filters.append(u"date:'%s'" % settings.DATETIME_FORMAT)
        return unicode(super(DateTimeAdaptor, self).render_value(value=value))


class TimeAdaptor(BaseAdaptor):
    """TimeField adaptor
    """
    def __init__(self, *args, **kwargs):
        super(TimeAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'charField'})

    def render_value(self, value=None):
        return unicode(value or '')

#   def set_value(self, value):
#       self.field_value = value
#       setattr(self.obj, self.get_real_field_name(), unicode(value))
#       return value
