# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689

# This code is setting up a WSGI (Web Server Gateway Interface) application for a Django project.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Deployment.settings')

application = get_wsgi_application()
