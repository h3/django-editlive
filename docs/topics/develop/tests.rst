Behavior Driven Testing
+++++++++++++++++++++++


As editlive is a Interface component, a BTD approach is used for testing it.

This gives this project the following benefits:

* Writing test is *really* easy. Non-programmers could almost write them.
* It tests the client and the backend at the same time, like a real user would
* It allow real world testing in multiple browsers (but currently only in Firefox and Chrome are tested)

`Travis CI`_ is used as build server. Not only you can see the current build status and the complete history, but you
can see the build status of branches and pull requests.

.. _Travis CI: https://travis-ci.org/h3/django-editlive

The test suite is a mix of Lettuce, Selenium and Splinter.

.. sidebar:: Tip for committers

    If you send pull request to this project for things that does not requires testing, 
    like updating the documentation or fixing typos in comments, just add `[ci skip]` 
    in your commit message and a build wont be triggered on Travis CI.


Lettuce
^^^^^^^

Lettuce makes writing the test cases and scenarios very easy

**strings.feature**

.. code-block:: python

    Feature: Manipulate strings
      In order to have some fun
      As a programming beginner
      I want to manipulate strings

      Scenario: Uppercased strings
        Given I have the string "lettuce leaves"
        When I put it in upper case
        Then I see the string is "LETTUCE LEAVES"

**steps**

.. code-block:: python

    from lettuce import *
    @step('I have the string "(.*)"')
    def have_the_string(step, string):
        world.string = string

    @step('I put it in upper case')
    def put_it_in_upper(step):
        world.string = world.string.upper()

    @step('I see the string is "(.*)"')
    def see_the_string_is(step, expected):
        assert world.string == expected, \
            "Got %s" % world.string


For more information about using Lettuce with Django consult the `Lettuce documentation`_.

.. _Lettuce documentation: http://lettuce.it/index.html


Splinter
^^^^^^^^

From its website: "*Splinter is an open source tool for testing web applications using Python. 
It lets you automate browser actions, such as visiting URLs and interacting with their items.*"

.. code-block:: python

     from splinter import Browser 
     browser = Browser() 
     # Visit URL 
     url = "http://www.google.com" 
     browser.visit(url) 
     browser.fill('q', 'splinter - python acceptance testing for web applications') 
     # Find and click the 'search' button 
     button = browser.find_by_name('btnK') 
     # Interact with elements 
     button.click() 
     if browser.is_text_present('splinter.cobrateam.info'): 
         print "Yes, the official website was found!" 
     else: 
         print "No, it wasn't found... We need to improve our SEO techniques" 
     browser.quit() 

For more infos `about Splinter`_.

.. _about Splinter: http://lettuce.it/index.html


Selenium
^^^^^^^^

From its website: "*Selenium automates browsers. That's it. What you do with that power is entirely up 
to you. Primarily it is for automating web applications for testing purposes, but is certainly not 
limited to just that. Boring web-based administration tasks can (and should!) also be automated as well.*"


For more infos `about Selenium`_.

.. _about Selenium: http://seleniumhq.org/


Bootstrapping
-------------


**Create a virtual env**

.. code-block:: bash

    cd django-editlive/
    virtualenv --distribute --no-site-packages editlive_test_env
    source editlive_test_env/bin/activate


**Install requirements**

.. code-block:: bash

    pip install -r docs/requirements.txt
    pip install -r example_project/requirements.txt


**Install Google Chrome & Google Chrome Webdriver (Ubuntu 12)**

.. code-block:: bash

  # Install Google Chrome (if not already installed!)
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb
  sudo apt-get install libgconf2-4
  sudo dpkg -i google-chrome*.deb

  # Install the Google Chrome webdriver
  wget https://chromedriver.googlecode.com/files/chromedriver_linux32_23.0.1240.0.zip
  unzip chromedriver_linux32_23.0.1240.0.zip
  mv chromedriver /usr/local/bin


Running the tests
-----------------


**With Google Chrome**

.. code-block:: bash

    cd example_project/

    export BROWSER="CHROME"
    ./run-tests

**With Google Firefox**

.. code-block:: bash
    
    export BROWSER="FIREFOX"
    ./run-tests


*Note*: Google Chrome is used as default.

**Test command arguments**

If you have special arguments to pass to the test runner you will 
have to use the full command:

.. code-block:: bash

    python manage.py harvest

To test a single feature:

.. code-block:: bash

    python manage.py harvest test_app/features/date.feature

Excluding applications:

.. code-block:: bash

    python manage.py harvest -A myApp1,myApp2


For a complete argument documentation, please refer to `this section of the Lettuce documentation`_.

.. _this section of the Lettuce documentation: http://lettuce.it/recipes/django-lxml.html#run-the-tests

