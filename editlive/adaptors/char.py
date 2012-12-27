from editlive.adaptors.base import BaseAdaptor


class CharAdaptor(BaseAdaptor):

    def __init__(self, *args, **kwargs):
        super(CharAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'charField'})
