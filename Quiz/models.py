from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

import random

class Pregunta(models.Model):
    NUMER_DE_RESPUESTAS_PERMITIDAS = 1

    texto = models.TextField(verbose_name='Texto de la pregunta')
    max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje', default=3, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.texto 


class ElegirRespuesta(models.Model):
    MAXIMO_RESPUESTA = 4

    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    def __str__(self):
        return self.texto


class Quiz(models.Model):
    nombre = models.CharField(max_length=255)
    preguntas = models.ManyToManyField(Pregunta, related_name='quizes')

    def __str__(self):
        return self.nombre


class QuizUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    quizes = models.ManyToManyField(Quiz, through='QuizSesion')
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

    #... tus métodos ...


class QuizSesion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='sesiones')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True)

    def finalizar(self):
        self.fecha_fin = timezone.now()
        self.save()

class PreguntasRespondidas(models.Model):
    sesion_quiz = models.ForeignKey(QuizSesion, on_delete=models.CASCADE, related_name='intentos')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)
