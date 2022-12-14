"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
application = get_wsgi_application()

if not settings.DEBUG:
    try:
        from dj_static import Cling
        application = Cling(get_wsgi_application())
    except:
        pass

# application = Cling(get_wsgi_application())

