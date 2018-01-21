"""
WSGI config for movieweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieweb.settings")

from movieweb.settings import DEBUG


application = get_wsgi_application()

if not DEBUG:    # Running on Heroku
    from dj_static import Cling
    application = Cling(get_wsgi_application())
