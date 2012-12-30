Adaptors
++++++++

Adaptor are special class which are used as abstract API to work with 
editlive objects. They provide basic functionnalities such as rendering, 
validating and updating an object. Each django field types can have its own 
adaptor.

Currently, the following adaptors are provided as default:

.. toctree::
   adaptors/base
   adaptors/boolean
   adaptors/char
   adaptors/choices
   adaptors/date
   adaptors/foreignkey
   adaptors/manytomany
   adaptors/text
