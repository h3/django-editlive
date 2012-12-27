from editlive.adaptors.base import BaseAdaptor


class BooleanAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(BooleanAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'booleanField'})

    def get_value(self):
        if callable(self.field_value):
            v = self.field_value()
        v = self.field_value
        return v and 'on' or 'off'

    def set_value(self, value):
        self.field_value = value
        setattr(self.obj, self.field_name, self.field_value)
        return value
