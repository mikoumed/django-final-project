"""
WSGI config for headlines project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'headlines.settings.prod'



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'headlines.settings.prod')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
