from editlive.adaptors.base import BaseAdaptor


class TextAdaptor(BaseAdaptor):
    def __init__(self, *args, **kwargs):
        super(TextAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'textField'})
