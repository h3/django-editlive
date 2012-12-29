Contributing to JavaScript documentation
++++++++++++++++++++++++++++++++++++++++

Installing requirements
-----------------------

Using Ubuntu One is really not a requirement, just a convenience for me.

::
    mkdir -p ~/Ubuntu\ One/SDKs/ && cd ~/Ubuntu\ One/SDKs/
    wget http://jsdoc-toolkit.googlecode.com/files/jsdoc_toolkit-2.4.0.zip
    unzip jsdoc_toolkit-2.4.0.zip
    cd jsdoc_toolkit-2.4.0
    

Compiling docs
--------------
::
    java -jar ~/Ubuntu\ One/SDKs/jsdoc_toolkit-2.4.0/jsdoc-toolkit/jsrun.jar \
    ~/Ubuntu\ One/SDKs/jsdoc_toolkit-2.4.0/jsdoc-toolkit/app/run.js ./ \
    --template=_themes/jsdoc-for-sphinx -x=js,jsx --directory=./jsdoc


    java -jar ~/Ubuntu\ One/SDKs/jsdoc_toolkit-2.4.0/jsdoc-toolkit/jsrun.jar \
    ~/Ubuntu\ One/SDKs/jsdoc_toolkit-2.4.0/jsdoc-toolkit/app/run.js ./ \
    --template=./docs/_themes/jsdoc-for-sphinx -x=js,jsx --directory=./docs/jsdoc

Including documentation
-----------------------
::
    .. include:: jsdoc/MyJavascriptClass.rst
       :start-after: class-methods

Tags reference
--------------

    **@_@augments** - Indicate this class uses another class as its "base."
    **@_@author** - Indicate the author of the code being documented.
    **@_@argument** - Deprecated synonym for **@_@param**.
    **@_@borrows** that as this - Document that class's member as if it were a member of this class.
    **@_@class** - Provide a description of the class (versus the constructor).
    **@_@constant** - Indicate that a variable's value is a constant.
    **@_@constructor** - Identify a function is a constructor.
    **@_@constructs** - Identicate that a lent function will be used as a constructor.
    **@_@default** - Describe the default value of a variable.
    **@_@deprecated** - Indicate use of a variable is no longer supported.
    **@_@description** - Provide a description (synonym for an untagged first-line).
    **@_@event** - Describe an event handled by a class.
    **@_@example** - Provide a small code example, illustrating usage.
    **@_@extends** - Synonym for **@_@augments**.
    **@_@field** - Indicate that the variable refers to a non-function.
    **@_@fileOverview** - Provides information about the entire file.
    **@_@function** - Indicate that the variable refers to a function.
    **@_@ignore** - Indicate JsDoc Toolkit should ignore the variable.
    **@_@inner** - Indicate that the variable refers to an inner function (and so is also **@_@private**).
    **@_@lends** - Document that all an object literal's members are members of a given class.
    {**@_@link** ...} - Like **@_@see** but can be used within the text of other tags.
    **@_@memberOf** - Document that this variable refers to a member of a given class.
    **@_@name** - Force JsDoc Toolkit to ignore the surrounding code and use the given variable name instead.
    **@_@namespace** - Document an object literal is being used as a "namespace."
    **@_@param** - Describe a function's parameter.
    **@_@private** - Indicate a variable is private (use the -p command line option to include these).
    **@_@property** - Document a property of a class from within the constructor's doclet.
    **@_@public** - Indicate an inner variable is public.
    **@_@requires** - Describe a required resource.
    **@_@returns** - Describe the return value of a function.
    **@_@see** - Describe a related resource.
    **@_@since** - Indicate that a feature has only been available on and after a certain version number.
    **@_@static** - Indicate that accessing the variable does not require instantiation of its parent.
    **@_@throws** - Describe the exception that a function might throw.
    **@_@type** - Describe the expected type of a variable's value or the value returned by a function.
    **@_@version** - Indicate the release version of this code. 


References
==========

 * https://github.com/stdbrouw/jsdoc-for-sphinx
 * http://code.google.com/p/jsdoc-toolkit/

