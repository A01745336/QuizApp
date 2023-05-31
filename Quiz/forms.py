# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689

# This code is importing necessary modules and classes for creating forms in Django.
from django import forms

from .models import  Pregunta, ElegirRespuesta, PreguntasRespondidas

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, get_user_model


# `User = get_user_model()` is a line of code that retrieves the user model that is currently active
# in the Django project. This is useful because it allows the code to reference the user model without
# having to hardcode the model name, which can be changed in the future.
User = get_user_model()

# This is a custom formset class in Python that validates the number of correct answers in a set of
# forms.
class ElegirInlineFormset(forms.BaseInlineFormSet):
	def clean(self):
		super(ElegirInlineFormset, self).clean()

		respuesta_correcta = 0
		for formulario in self.forms:
			if not formulario.is_valid():
				return

			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta += 1

		try:
			assert respuesta_correcta == Pregunta.NUMER_DE_RESPUESTAS_PERMITIDAS
		except AssertionError:
			raise forms.ValidationError('Exactamente una sola respuesta es permitida')


# This is a Python class for a user login form that validates the username and password entered by the
# user.
class UsuarioLoginFormulario(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Este usuario No existe")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("Este Usuario No esta activo")

		return super(UsuarioLoginFormulario, self).clean(*args, **kwargs)



# The class `RegistroFormulario` is a form for registering a new user with required fields for email,
# first name, last name, username, and password.
class RegistroFormulario(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)

	class Meta:
		model = User 

		fields = [

			'first_name',
			'last_name',
			'username',
			'email',
			'password1',
			'password2'

		]