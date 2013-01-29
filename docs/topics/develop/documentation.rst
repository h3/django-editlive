Contributing to documentation
+++++++++++++++++++++++++++++

You see that `build` script in the docs folder ? Don't use it.

That is, unless you have followed the instructions on how to compile the JavaScript 
documentation and placed the `sdoc_toolkit-2.4.0` in a folder named `~/Ubuntu\ One/SDKs`.

I might give the build script some attention some day and make it more useful, but for 
now I have other priorities.


Writing documentation
---------------------

You can find documentation in three places in this project:

* In Python docstring
* In JavaScript comments of the editlive widgets
* And finally in the `docs/` folder

So if you submit a pull request, it's quite easy to update the documentation for the code 
you are submitting. You just have to comment the code properly.


Building the Python documentation
-------------------------------------

.. code-block:: bash

    cd django-editlive/docs/
    make html


Building the JavaScript documentation
-------------------------------------

This is only needed if changes have been made to a JavaScript file.

Installing requirements
^^^^^^^^^^^^^^^^^^^^^^^

Using Ubuntu One is really not a requirement, just a convenience for me.

.. code-block:: bash

    mkdir -p ~/Ubuntu\ One/SDKs/ && cd ~/Ubuntu\ One/SDKs/
    wget http://jsdoc-toolkit.googlecode.com/files/jsdoc_toolkit-2.4.0.zip
    unzip jsdoc_toolkit-2.4.0.zip
    cd jsdoc_toolkit-2.4.0
    

Compiling docs
^^^^^^^^^^^^^^

.. code-block:: bash
    
    cd django-editlive/
    java -jar ~/Ubuntu\ One/SDKs/jsdoc_toolkit-2.4.0/jsdoc-toolkit/jsrun.jar \
    ~/Ubuntu\ One/SDKs/jsdoc_toolkit-2.4.0/jsdoc-toolkit/app/run.js ./ \
    --template=_themes/jsdoc-for-sphinx -x=js,jsx --directory=./jsdoc

..
    java -jar ~/Ubuntu\ One/SDKs/jsdoc_toolkit-2.4.0/jsdoc-toolkit/jsrun.jar \
    ~/Ubuntu\ One/SDKs/jsdoc_toolkit-2.4.0/jsdoc-toolkit/app/run.js ./ \
    --template=./docs/_themes/jsdoc-for-sphinx -x=js,jsx --directory=./docs/jsdoc

Including documentation
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: rest

    .. include:: jsdoc/MyJavascriptClass.rst
       :start-after: class-methods

Tags reference
^^^^^^^^^^^^^^

* **@augments** - Indicate this class uses another class as its "base."
* **@author** - Indicate the author of the code being documented.
* **@argument** - Deprecated synonym for **@param**.
* **@borrows** that as this - Document that class's member as if it were a member of this class.
* **@class** - Provide a description of the class (versus the constructor).
* **@constant** - Indicate that a variable's value is a constant.
* **@constructor** - Identify a function is a constructor.
* **@constructs** - Identicate that a lent function will be used as a constructor.
* **@default** - Describe the default value of a variable.
* **@deprecated** - Indicate use of a variable is no longer supported.
* **@description** - Provide a description (synonym for an untagged first-line).
* **@event** - Describe an event handled by a class.
* **@example** - Provide a small code example, illustrating usage.
* **@extends** - Synonym for **@augments**.
* **@field** - Indicate that the variable refers to a non-function.
* **@fileOverview** - Provides information about the entire file.
* **@function** - Indicate that the variable refers to a function.
* **@ignore** - Indicate JsDoc Toolkit should ignore the variable.
* **@inner** - Indicate that the variable refers to an inner function (and so is also **@private**).
* **@lends** - Document that all an object literal's members are members of a given class.
* {**@link** ...} - Like **@see** but can be used within the text of other tags.
* **@memberOf** - Document that this variable refers to a member of a given class.
* **@name** - Force JsDoc Toolkit to ignore the surrounding code and use the given variable name instead.
* **@namespace** - Document an object literal is being used as a "namespace."
* **@param** - Describe a function's parameter.
* **@private** - Indicate a variable is private (use the -p command line option to include these).
* **@property** - Document a property of a class from within the constructor's doclet.
* **@public** - Indicate an inner variable is public.
* **@requires** - Describe a required resource.
* **@returns** - Describe the return value of a function.
* **@see** - Describe a related resource.
* **@since** - Indicate that a feature has only been available on and after a certain version number.
* **@static** - Indicate that accessing the variable does not require instantiation of its parent.
* **@throws** - Describe the exception that a function might throw.
* **@type** - Describe the expected type of a variable's value or the value returned by a function.
* **@version** - Indicate the release version of this code. 

References
^^^^^^^^^^

* `Sphinx - Python documentation generator`_ 
* `Sphinx - Include documentation from docstrings`_
* `JSDOC - A documentation generator for JavaScript`_ 
* `JSDOC for Sphinx`_

.. _JSDOC - A documentation generator for JavaScript: http://code.google.com/p/jsdoc-toolkit/
.. _JSDOC for Sphinx: https://github.com/stdbrouw/jsdoc-for-sphinx
.. _Sphinx - Python documentation generator: http://sphinx-doc.org/
.. _Sphinx - Include documentation from docstrings: http://sphinx-doc.org/ext/autodoc.html
