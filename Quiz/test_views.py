from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import QuizUsuario, Pregunta, PreguntasRespondidas


class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.quiz_user = QuizUsuario.objects.create(usuario=self.user)

    def test_inicio_view(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inicio.html')

    def test_home_usuario_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('HomeUsuario'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Usuario/home.html')

    def test_tablero_view(self):
        response = self.client.get(reverse('tablero'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'play/tablero.html')

    def test_jugar_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('jugar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'play/jugar.html')

    def test_jugar_view_post(self):
        pregunta = Pregunta.objects.create(texto_pregunta='Test question')
        respuesta = pregunta.opciones.create(texto_opcion='Test option', correcta=True)
        pregunta_respondida = PreguntasRespondidas.objects.create(pregunta=pregunta, quiz_user=self.quiz_user)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('jugar'), {'pregunta_pk': pregunta.pk, 'respuesta_pk': respuesta.pk})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.quiz_user.intentos.count(), 2)  # Additional attempt created
        self.assertEqual(self.quiz_user.cantidad_preguntas, 0)  # All questions answered

    def test_resultado_pregunta_view(self):
        pregunta_respondida = PreguntasRespondidas.objects.create(pregunta=Pregunta(), quiz_user=self.quiz_user)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('resultado', args=[pregunta_respondida.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'play/resultados.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Usuario/login.html')

    def test_registro_view_get(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Usuario/registro.html')

    def test_registro_view_post(self):
        response = self.client.post(reverse('registro'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
