
.. _test-and-dev-env:

Testing and development environment
+++++++++++++++++++++++++++++++++++

An example project is included to provide quick bootstraping of
a development and testing environment.


Create a virtualenv
-------------------

.. code-block:: bash

    cd django-editlive/
    virtualenv --distribute --no-site-packages editlive_test_env
    source editlive_test_env/bin/activate


Install requirements
--------------------

.. code-block:: bash

    pip install -r docs/requirements.txt
    pip install -r example_project/requirements.txt


Install Google Chrome & Google Chrome Webdriver
-----------------------------------------------

**Note:** This installation has only been tested on Ubuntu 12+.

.. code-block:: bash

  # Install Google Chrome (if not already installed!)
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb
  sudo apt-get install libgconf2-4
  sudo dpkg -i google-chrome*.deb

  # Install the Google Chrome webdriver
  wget https://chromedriver.googlecode.com/files/chromedriver_linux32_23.0.1240.0.zip
  unzip chromedriver_linux32_23.0.1240.0.zip
  mv chromedriver /usr/local/bin
