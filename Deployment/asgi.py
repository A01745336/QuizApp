

# This code is setting up the ASGI (Asynchronous Server Gateway Interface)
# application for a Django
# project.
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Deployment.settings')

application = get_asgi_application()
