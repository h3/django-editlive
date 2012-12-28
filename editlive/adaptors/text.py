from editlive.adaptors.base import BaseAdaptor


class TextAdaptor(BaseAdaptor):
    """The TextAdaptor is used for Text fields.
    """
    def __init__(self, *args, **kwargs):
        super(TextAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'textField'})
