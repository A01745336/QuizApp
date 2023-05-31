import unittest
from django.test import TestCase
from django.contrib import admin
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUsuario

# Unregister the QuizUsuario and PreguntasRespondidas models from the admin site
admin.site.unregister(QuizUsuario)
admin.site.unregister(PreguntasRespondidas)
admin.site.unregister(Pregunta)
admin.site.unregister(ElegirRespuesta)

class QuizModelsTestCase(TestCase):
    def setUp(self):
        # Set up test data
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create a quiz for the user
        self.quiz = QuizUsuario.objects.create(usuario=self.user)

        # Create a question for the quiz
        self.pregunta = Pregunta.objects.create(
            texto='What is the capital of France?',
            quiz=self.quiz
        )

        # Create answer choices for the question
        self.respuesta1 = ElegirRespuesta.objects.create(
            pregunta=self.pregunta,
            texto='Paris',
            correcta=True
        )
        self.respuesta2 = ElegirRespuesta.objects.create(
            pregunta=self.pregunta,
            texto='London',
            correcta=False
        )


if __name__ == '__main__':
    unittest.main()
