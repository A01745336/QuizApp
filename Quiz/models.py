from django.db import models
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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    preguntas = models.ManyToManyField(Pregunta, related_name='quizes')

    def __str__(self):
        return f"Quiz - {self.usuario.username}"


class PreguntasRespondidas(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return f"{self.quiz} - Pregunta: {self.pregunta}"


class QuizUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

    def crear_intentos(self, pregunta):
        intento = PreguntasRespondidas(pregunta=pregunta, quiz=self)
        intento.save()

    def obtener_nuevas_preguntas(self):
        respondidas = PreguntasRespondidas.objects.filter(quiz=self).values_list('pregunta__pk', flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)

    def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
            return

        pregunta_respondida.respuesta = respuesta_seleccionada
        if respuesta_seleccionada.correcta:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje_obtenido = respuesta_seleccionada.pregunta.max_puntaje
        else:
            pregunta_respondida.correcta = False
            pregunta_respondida.puntaje_obtenido = 0

        pregunta_respondida.save()

        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(total_puntaje=models.Sum('puntaje_obtenido'))['total_puntaje']

        if puntaje_actualizado is not None:
            self.puntaje_total = puntaje_actualizado
        else:
            self.puntaje_total = 0

        self.save()
