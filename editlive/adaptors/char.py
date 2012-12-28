"""
.. module:: CharAdaptor
.. moduleauthor:: Maxime Haineault <max@motion-m.ca>
"""

from editlive.adaptors.base import BaseAdaptor


class CharAdaptor(BaseAdaptor):
    """The CharAdaptor is used for CharField and unknown field types".
    """

    def __init__(self, *args, **kwargs):
        super(CharAdaptor, self).__init__(*args, **kwargs)
        if self.form_field:
            self.attributes.update({'data-type': 'charField'})
