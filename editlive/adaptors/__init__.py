"""Adaptors

.. moduleauthor:: Maxime Haineault <max@motion-m.ca>

"""
from editlive.adaptors.char import BaseAdaptor
from editlive.adaptors.char import CharAdaptor
from editlive.adaptors.boolean import BooleanAdaptor
from editlive.adaptors.choices import ChoicesAdaptor
from editlive.adaptors.date import DateAdaptor, DateTimeAdaptor, TimeAdaptor
from editlive.adaptors.foreignkey import ForeignKeyAdaptor
from editlive.adaptors.inlines import StackedInlineAdaptor, TabularInlineAdaptor
from editlive.adaptors.manytomany import ManyToManyAdaptor
from editlive.adaptors.text import TextAdaptor
