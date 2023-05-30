from django.urls import path

from .views import (
            inicio, 
            registro, 
            loginView, 
            logout_vista,
            HomeUsuario, 
            jugar,
            resultado,  # Esto fue cambiado de `resultado_pregunta` a `resultado`
            tablero)

urlpatterns = [
    
    path('', inicio, name='inicio'),
    path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),

    path('login/', loginView, name='login'),
    path('logout_vista/', logout_vista, name='logout_vista'),
    path('registro/', registro, name='registro'),
    path('tablero/', tablero, name='tablero'),
	path('resultado/', resultado, name='resultado'),

    
    path('jugar/', jugar, name='jugar'),
    path('resultado/<int:pregunta_respondida_pk>/', resultado, name='resultado'),  # Esto también fue cambiado

]
