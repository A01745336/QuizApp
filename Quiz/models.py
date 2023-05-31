# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689

# Importing the `models` module from Django's database abstraction layer and the `User` model from
# Django's built-in authentication system.
from django.db import models
from django.contrib.auth.models import User

# This is a Django model class for a question with a text field and maximum score.
class Pregunta(models.Model):
    NUMER_DE_RESPUESTAS_PERMITIDAS = 1

    texto = models.TextField(verbose_name='Texto de la pregunta')
    max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje', default=3, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.texto 


# This is a model class for choosing a response with a maximum of 4 options, related to a question and
# with a boolean field indicating if it's the correct answer.
class ElegirRespuesta(models.Model):
    MAXIMO_RESPUESTA = 4

    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    def __str__(self):
        return self.texto


# The QuizUsuario class defines methods for creating quiz attempts, getting new quiz questions, and
# validating quiz attempts for a user.
class QuizUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)
    cantidad_preguntas = models.PositiveIntegerField(verbose_name='Cantidad de preguntas', default=0)

    def crear_intentos(self, pregunta):
        intento = PreguntasRespondidas(pregunta=pregunta, quizUser=self)
        intento.save()

    def obtener_nuevas_preguntas(self, cantidad_preguntas):
        respondidas = PreguntasRespondidas.objects.filter(quizUser=self).values_list('pregunta__pk', flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas).order_by('?')[:cantidad_preguntas]
        return preguntas_restantes

    def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
            return

        pregunta_respondida.respuesta_seleccionada = respuesta_seleccionada
        if respuesta_seleccionada.correcta:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje_obtenido = respuesta_seleccionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_seleccionada
        else:
            pregunta_respondida.respuesta = respuesta_seleccionada
            pregunta_respondida.puntaje_obtenido = 0

        pregunta_respondida.save()

        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        """
        This function updates the total score of a user based on their correct attempts.
        """
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(
            total_puntaje=models.Sum('puntaje_obtenido'))['total_puntaje']

        if puntaje_actualizado is not None:
            self.puntaje_total = puntaje_actualizado
        else:
            self.puntaje_total = 0

        self.save()


# This is a model class for storing answered questions in a quiz, including the user, question, chosen
# answer, correctness, and obtained score.
class PreguntasRespondidas(models.Model):
    quizUser = models.ForeignKey(QuizUsuario, on_delete=models.CASCADE, related_name='intentos')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)
