from os import environ


ENVIRONMENT_SETTINGS = [
    "DATABASE_PASSWORD",
    "VIRTUALENV_NAME",
]


def env_settings():
    d = {}
    for s in ENVIRONMENT_SETTINGS:
        if s in environ:
            d[s] = environ[s]
    return d
