# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689
from django.urls import reverse, resolve
from django.test import TestCase
from Quiz.views import inicio, registro, loginView, logout_vista, HomeUsuario, jugar, resultado_pregunta, tablero

class TestUrls(TestCase):

    def test_inicio_url(self):
        """
        This is a unit test in Python that checks if the URL for 'inicio' resolves to the correct function.
        """
        path = reverse('inicio')
        self.assertEqual(resolve(path).func, inicio)

    def test_registro_url(self):
        """
        This function tests whether the URL for the "registro" page resolves to the correct view function.
        """
        path = reverse('registro')
        self.assertEqual(resolve(path).func, registro)

    def test_login_url(self):
        """
        This function tests whether the URL for the login page resolves to the correct view function.
        """
        path = reverse('login')
        self.assertEqual(resolve(path).func, loginView)

    def test_logout_url(self):
        """
        This function tests whether the URL for logging out resolves to the correct view function.
        """
        path = reverse('logout_vista')
        self.assertEqual(resolve(path).func, logout_vista)

    def test_HomeUsuario_url(self):
        """
        This function tests whether the URL for the "HomeUsuario" page resolves to the correct view
        function.
        """
        path = reverse('HomeUsuario')
        self.assertEqual(resolve(path).func, HomeUsuario)

    def test_jugar_url(self):
        """
        This function tests if the URL for playing a game resolves to the correct view function.
        """
        path = reverse('jugar')
        self.assertEqual(resolve(path).func, jugar)

    def test_resultado_pregunta_url(self):
        """
        This function tests if the URL for the "resultado" view with a specific argument resolves to the
        correct function.
        """
        path = reverse('resultado', args=[1])  # passing 1 as the pregunta_respondida_pk argument
        self.assertEqual(resolve(path).func, resultado_pregunta)

    def test_tablero_url(self):
        """
        This function tests whether the URL for the "tablero" view resolves to the correct function.
        """
        path = reverse('tablero')
        self.assertEqual(resolve(path).func, tablero)
