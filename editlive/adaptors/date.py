from editlive.conf import settings
from editlive.adaptors.base import BaseAdaptor


class DateAdaptor(BaseAdaptor):
    """DateField adaptor

    Uses the following setting:

    `settings.EDITLIVE_DATE_FORMAT`

    """
    def __init__(self, *args, **kwargs):
        super(DateAdaptor, self).__init__(*args, **kwargs)
        field = self.form.fields.get(self.field_name)
        if field:
            self.attributes.update({'data-format': '%s' % field.widget.format})
            self.attributes.update({'data-date-format': '%s' % settings.DATE_WIDGET_FORMAT})
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

    Uses the following setting:

    `settings.EDITLIVE_DATE_FORMAT`
    `settings.EDITLIVE_TIME_FORMAT`

    """
    def __init__(self, *args, **kwargs):
        super(DateTimeAdaptor, self).__init__(*args, **kwargs)
        field = self.form.fields.get(self.field_name)
        if field:
            self.attributes.update({'data-format': '%s' % field.widget.format})
            self.attributes.update({'data-date-format': '%s' % settings.DATE_WIDGET_FORMAT})
            self.attributes.update({'data-time-format': '%s' % settings.TIME_WIDGET_FORMAT})
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

    Uses the following setting:

    `settings.EDITLIVE_TIME_FORMAT`

    """
    def __init__(self, *args, **kwargs):
        super(TimeAdaptor, self).__init__(*args, **kwargs)
        field = self.form.fields.get(self.field_name)
        if field:
            self.attributes.update({'data-format': '%s' % field.widget.format})
            self.attributes.update({'data-time-format': '%s' % settings.TIME_WIDGET_FORMAT})
        if self.form_field:
            self.attributes.update({'data-type': 'charField'}) #  TODO: timeField

    def render_value(self, value=None):
        return unicode(value or '')

#   def set_value(self, value):
#       self.field_value = value
#       setattr(self.obj, self.get_real_field_name(), unicode(value))
#       return value
