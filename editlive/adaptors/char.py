"""
.. module:: CharAdaptor
.. moduleauthor:: Maxime Haineault <max@motion-m.ca>
"""

from editlive.adaptors.base import BaseAdaptor


class CharAdaptor(BaseAdaptor):
    """The CharAdaptor is the most generic adaptor. It subclass the 
    BaseAdaptor and only alter the `data-type` attribute and set it 
    to "charField".

    .. note::

       The CharAdaptor is used as default when there is no specific 
       adaptor for a given field type.

    """

    def __init__(self, *args, **kwargs):
        super(CharAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'charField'})

#   def hello(self, test, test2='blah'):
#       """This gets the foobar

#       This really should have a full function definition, but I am too lazy.

#       >>> print get_foobar(10, 20)
#       30
#       >>> print get_foobar('a', 'b')
#       ab

#       Isn't that what you want?

#       """
#       print "yay"
