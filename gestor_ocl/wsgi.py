"""
WSGI config for gestor_ocl project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
import os
from os.path import join, dirname, abspath

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
from whitenoise.django import DjangoWhiteNoise

dotenv_path = join(dirname(dirname(abspath(__file__))), '.env')
load_dotenv(dotenv_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestor_ocl.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
