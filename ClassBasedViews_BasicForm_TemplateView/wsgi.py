"""
WSGI config for ClassBasedViews_BasicForm_TemplateView project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ClassBasedViews_BasicForm_TemplateView.settings')

application = get_wsgi_application()
