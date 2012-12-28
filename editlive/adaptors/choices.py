from editlive.adaptors.base import BaseAdaptor


class ChoicesAdaptor(BaseAdaptor):
    """The ChoicesAdaptor is used for fields with a `choices` argument. 
    """

    def __init__(self, *args, **kwargs):
        super(ChoicesAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'choicesField'})

    def get_value(self):
        """Instead of returning the field value we call and 
        return the object's `get_FIELD_display` method.
        """
        if callable(self.field_value):
            return self.field_value()
        return getattr(self.obj, 'get_%s_display' % self.field.name)()
