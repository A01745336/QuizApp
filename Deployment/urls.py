# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689
# This code is defining the URL patterns for a Django web application.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Quiz.urls'))
]
