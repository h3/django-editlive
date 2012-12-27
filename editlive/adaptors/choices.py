from editlive.adaptors.base import BaseAdaptor


class ChoicesAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(ChoicesAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'choicesField'})

    def get_value(self):
        if callable(self.field_value):
            return self.field_value()
        return getattr(self.obj, 'get_%s_display' % self.field.name)()

