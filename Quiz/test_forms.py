from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import UsuarioLoginFormulario, RegistroFormulario

User = get_user_model()

class UsuarioLoginFormularioTest(TestCase):
    def test_valid_login_form(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        form = UsuarioLoginFormulario(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_login_form(self):
        form_data = {
            'username': 'testuser',
            'password': ''
        }
        form = UsuarioLoginFormulario(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['password'][0], 'This field is required.')

class RegistroFormularioTest(TestCase):
    def test_valid_registration_form(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = RegistroFormulario(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        form_data = {
            'first_name': '',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'differentpassword'
        }
        form = RegistroFormulario(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['password2'][0], "Las contraseñas no coinciden.")

class CustomFormsetTest(TestCase):
    def test_valid_formset(self):
        form_data = [
            {
                'respuesta': 'Respuesta 1',
                'correcta': True
            },
            {
                'respuesta': 'Respuesta 2',
                'correcta': False
            },
            {
                'respuesta': 'Respuesta 3',
                'correcta': False
            }
        ]
        formset = ElegirInlineFormset(data=form_data)
        self.assertTrue(formset.is_valid())

    def test_invalid_formset(self):
        form_data = [
            {
                'respuesta': 'Respuesta 1',
                'correcta': True
            },
            {
                'respuesta': '',
                'correcta': False
            },
            {
                'respuesta': 'Respuesta 3',
                'correcta': True
            }
        ]
        formset = ElegirInlineFormset(data=form_data)
        self.assertFalse(formset.is_valid())
        self.assertEqual(len(formset.errors), 2)
        self.assertEqual(formset.errors[1]['respuesta'][0], 'This field is required.')
        self.assertEqual(formset.errors[2]['correcta'][0], 'Este campo es obligatorio.')

class UserModelTest(TestCase):
    def test_create_user(self):
        User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
