from editlive.adaptors.base import BaseAdaptor


class ForeignKeyAdaptor(BaseAdaptor):

    def __init__(self, *args, **kwargs):
        super(ForeignKeyAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({
                'data-type':   'foreignkeyField',
                'data-source': '#%s' % self.attributes.get('data-field-id'),
            })

    def set_value(self, value):
        self.field_value = value
        setattr(self.obj, '%s_id' % \
                self.get_real_field_name(), self.field_value)
        return self.field_value

    def render_value(self, value=None):
        val = value or getattr(self.obj, self.get_real_field_name())
        rendered_val = '' if val is None else unicode(val)
        return rendered_val

