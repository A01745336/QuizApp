from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


# The above class contains test cases for various views in a Django web application.
class TestViews(TestCase):
    
    def setUp(self):
        """
        This function sets up various URLs and creates a test user for a Django test case.
        """
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testemail@test.com', 'testpassword')

        self.inicio_url = reverse('inicio')
        self.HomeUsuario_url = reverse('HomeUsuario')
        self.login_url = reverse('login')
        self.logout_vista_url = reverse('logout_vista')
        self.registro_url = reverse('registro')
        self.tablero_url = reverse('tablero')
        self.jugar_url = reverse('jugar')

    def test_inicio_view_GET(self):
        """
        This is a unit test function that checks if a GET request to a specific URL returns a 200 status
        code.
        """
        response = self.client.get(self.inicio_url)

        self.assertEquals(response.status_code, 200)
    
    def test_HomeUsuario_view_GET(self):
        """
        This function tests the GET request for the HomeUsuario view after logging in a test user.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.HomeUsuario_url)

        self.assertEquals(response.status_code, 200)

    def test_login_view_GET(self):
        """
        This function tests if the HTTP GET request to the login URL returns a status code of 200.
        """
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)

    def test_logout_vista_view_GET(self):
        """
        This function tests the GET request for logging out a user and expects a redirect status code.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_vista_url)

        self.assertEquals(response.status_code, 302)

    def test_registro_view_GET(self):
        """
        This is a unit test function that checks if a GET request to a registration URL returns a 200 status
        code.
        """
        response = self.client.get(self.registro_url)

        self.assertEquals(response.status_code, 200)

    def test_tablero_view_GET(self):
        """
        This function tests the GET request for a tablero view after logging in with a test user.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.tablero_url)

        self.assertEquals(response.status_code, 200)
        
    def test_jugar_view_GET(self):
        """
        This function tests the GET request for a "jugar" view after logging in with a test user.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.jugar_url)

        self.assertEquals(response.status_code, 200)
