# This is our default ordering, to provide an out-of-the-box running app.
# We check DJANGO_SETTINGS_MODULE, then try to import local (untracked), then dev.
#
# If you need a specific setting, use --settings, like:
# ./manage.py syncdb --settings=env.live
#

try:
    from os import environ
    import imp
    i = imp.find_module(environ["DJANGO_SETTINGS_MODULE"])
    imp.load_module(environ["DJANGO_SETTINGS_MODULE"])
except:
    import sys
    from os.path import dirname, abspath, join
    PROJECT_ROOT = dirname(__file__)
   #sys.path.insert(0, PROJECT_ROOT)
    sys.path.insert(0, abspath(join(PROJECT_ROOT, '../')))
    sys.path.insert(0, abspath(join(PROJECT_ROOT, '../../editlive/')))
    import example_project
    from example_project.envs.local import *
#   try:
#       from envs.local import *
#   except:
#       try:
#           from envs.dev import *
#       except:
#           raise Exception("No settings found! Please set up an env/local.py, or specify settings explicitly")
