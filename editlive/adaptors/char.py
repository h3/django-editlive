"""
.. module:: CharAdaptor
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>


"""

from editlive.adaptors.base import BaseAdaptor


class CharAdaptor(BaseAdaptor):
    """The CharAdaptor.

    .. note::

       The CharAdaptor subclass BaseAdaptor.

    """

    def __init__(self, *args, **kwargs):
        """The CharAdaptor is basically just the BaseAdaptor.

        Args:
           field (str): We all know what foo does.
           obj (obj): We all know what foo does.
           field_name (str): We all know what foo does.


        Kwargs:
           field_value (str): We all know what foo does.
           kwargs(dict): We all know what foo does.

        """
        super(CharAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'charField'})

    def hello(self, *args, **kwargs):
        """The CharAdaptor is basically just the BaseAdaptor.

        Args:
           field (str): We all know what foo does.
           obj (obj): We all know what foo does.
           field_name (str): We all know what foo does.


        Kwargs:
           field_value (str): We all know what foo does.
           kwargs(dict): We all know what foo does.

        """
        super(CharAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'charField'})
