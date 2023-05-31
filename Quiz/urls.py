# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689

# `from django.urls import path` is importing the `path` function from the `django.urls` module. This
# function is used to define URL patterns for a Django web application.
from django.urls import path

# This code is defining the URL patterns for a Django web application. It imports various views from
# the application's views.py file and maps them to specific URLs using the `path()` function.
from .views import (
			inicio, 
			registro, 
			loginView, 
			logout_vista,
			HomeUsuario, 
			jugar,
			resultado_pregunta,
			tablero)

urlpatterns = [
	
	path('', inicio, name='inicio'),
	path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),


	path('login/', loginView, name='login'),
	path('logout_vista/', logout_vista, name='logout_vista'),
	path('registro/', registro, name='registro'),
	path('tablero/', tablero, name='tablero'),

	
	path('jugar/', jugar, name='jugar'),
 	path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado'),

]