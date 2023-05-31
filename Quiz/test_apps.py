# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689

# tests.py or test_apps.py
# This is a test class that checks if the QuizConfig app name is 'Quiz'.
from django.apps import apps
from django.test import TestCase
from Quiz.apps import QuizConfig


class TestQuizConfig(TestCase):
    def test_apps(self):
        self.assertEqual(QuizConfig.name, 'Quiz')
        self.assertEqual(apps.get_app_config('Quiz').name, 'Quiz')
