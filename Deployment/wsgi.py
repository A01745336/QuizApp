

# This code is setting up a WSGI (Web Server Gateway Interface) application for a Django project.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Deployment.settings')

application = get_wsgi_application()
