# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689
from django.test import TestCase
from Quiz.forms import RegistroFormulario

class TestForms(TestCase):

    def test_registro_form_valid_data(self):
        """
        This function tests if a registration form with valid data is considered valid.
        """
        form = RegistroFormulario(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'john_doe',
            'email': 'john@example.com',
            'password1': 'complex_password',
            'password2': 'complex_password'
        })

        self.assertTrue(form.is_valid())

    def test_registro_form_no_data(self):
        """
        This function tests if a registration form is invalid when no data is provided.
        """
        form = RegistroFormulario(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)  # Assuming that all fields in your form are required

