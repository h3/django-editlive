
Create a virtual env::

    cd django-editlive/
    virtualenv --distribute --no-site-packages editlive_test_env
    source editlive_test_env/bin/activate

Install requirements::

    pip install -r requirements.txt
    pip install -r example_project/requirements.txt

Run the functional test suite::

    cd example_project/
    python manage.py harvest -A dajaxice,south,editlive
