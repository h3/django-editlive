from common import *

# Dev specific stuff
DEV = True
SITE_ID = 1

COMPRESS_OFFLINE = True
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'MEDIA_URL': MEDIA_URL,
}

#HIDE_DJANGO_SQL = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
   #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
   #'HIDE_DJANGO_SQL': True,
   #'ENABLE_STACKTRACES' : True,
}

MIDDLEWARE_CLASSES += MIDDLEWARE_CLASSES + (
   #'debug_toolbar.middleware.DebugToolbarMiddleware', 
)

INTERNAL_IPS = ('127.0.0.1',)

#INSTALLED_APPS = INSTALLED_APPS + (
#    'debug_toolbar',
#)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
