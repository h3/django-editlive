from editlive.adaptors.base import BaseAdaptor


class BooleanAdaptor(BaseAdaptor):
    """The BooleanAdaptor is used for BooleanField.

    .. note::

       Not tested with NullBooleanField.

    """

    def __init__(self, *args, **kwargs):
        super(BooleanAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'booleanField'})

    def get_value(self):
        """Instead of returning True or False we return 'on' or 'off'
        """
        if callable(self.field_value):
            v = self.field_value()
        v = self.field_value
        return v and 'on' or 'off'

#   def set_value(self, value):
#       self.field_value = value
#       setattr(self.obj, self.field_name, self.field_value)
#       return value
