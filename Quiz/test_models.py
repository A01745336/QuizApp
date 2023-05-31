
# Final Project: Quiz Application with Microservices
# Date: 30-May-2023
# Authors:
#           Diego Alejandro Balderas Tlahuitzo - A01745336
#           Gilberto André García Gaytán - A01753176
#           Paula Sophia Santoyo Arteaga - A01745312
#           Ricardo Ramírez Condado - A01379299
#           Paola Danae López Pérez- A01745689

from django.contrib import admin

from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUsuario

from .forms import ElegirInlineFormset


# This is an admin tabular inline class for choosing a response with a maximum and minimum number of
# responses and a custom formset.
class ElegirRespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.MAXIMO_RESPUESTA
    min_num = ElegirRespuesta.MAXIMO_RESPUESTA
    formset = ElegirInlineFormset



# This is a Django admin class for managing questions with inline answer choices and search
# functionality.
class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInline, )
    list_display = ['texto',]
    search_fields = ['texto', 'preguntas__texto']

# This is a Django admin model for displaying answered questions with their corresponding responses,
# correctness, and obtained score.
class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

# The class Meta is defining the model for PreguntasRespondidas.
    class Meta:
        model = PreguntasRespondidas


# This code is registering the `QuizUsuario` model with the Django admin site and creating an admin
# interface for it. The `QuizUsuarioAdmin` class is defining the display fields (`list_display`) and
# search fields (`search_fields`) for the model, as well as an action (`generar_preguntas`) that can
# be performed on selected instances of the model. The `generar_preguntas` method generates new
# questions for the selected users and creates attempts for each question.
@admin.register(QuizUsuario)
class QuizUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'puntaje_total']
    search_fields = ['usuario__username']
    actions = ['generar_preguntas']

    def generar_preguntas(self, request, queryset):
        """
        This function generates a specified number of questions for selected users and creates attempts for
        each question.
        
        :param request: The request parameter is an object that represents the HTTP request made by the
        user. It contains information such as the user's IP address, the HTTP method used (GET, POST, etc.),
        and any data submitted in the request. It is typically used in Django views and can be used to
        access session
        :param queryset: A queryset is a collection of objects that match certain criteria. In this case, it
        is a collection of QuizUser objects that have been selected by the user
        """
        cantidad_preguntas = int(input("Ingrese la cantidad de preguntas que desea generar: "))
        for quiz_user in queryset:
            preguntas = quiz_user.obtener_nuevas_preguntas(cantidad_preguntas)
            if preguntas:
                for pregunta in preguntas:
                    quiz_user.crear_intentos(pregunta)

    generar_preguntas.short_description = "Generar preguntas para los usuarios seleccionados"


# This code is registering the `PreguntasRespondidas`, `Pregunta`, and `ElegirRespuesta` models with
# the Django admin site and creating admin interfaces for them. The `PreguntasRespondidasAdmin` class
# is defining the display fields (`list_display`) for the `PreguntasRespondidas` model, while the
# `PreguntaAdmin` class is defining the display fields (`list_display`) and search fields
# (`search_fields`) for the `Pregunta` model, as well as an inline class (`ElegirRespuestaInline`) for
# managing answer choices. The `admin.site.register` function is used to register each model with its
# corresponding admin class.
admin.site.register(PreguntasRespondidas, PreguntasRespondidasAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)


from django.test import TestCase
from django.contrib.auth.models import User
from .models import Pregunta, ElegirRespuesta, QuizUsuario, PreguntasRespondidas


class ModelTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Crear una pregunta de prueba
        self.pregunta = Pregunta.objects.create(
            texto='¿Cuál es la capital de Francia?',
            max_puntaje=3
        )

        # Crear opciones de respuesta para la pregunta
        self.respuesta1 = ElegirRespuesta.objects.create(
            pregunta=self.pregunta,
            correcta=True,
            texto='París'
        )
        self.respuesta2 = ElegirRespuesta.objects.create(
            pregunta=self.pregunta,
            correcta=False,
            texto='Londres'
        )
        self.respuesta3 = ElegirRespuesta.objects.create(
            pregunta=self.pregunta,
            correcta=False,
            texto='Roma'
        )
        self.respuesta4 = ElegirRespuesta.objects.create(
            pregunta=self.pregunta,
            correcta=False,
            texto='Madrid'
        )

        # Crear un QuizUsuario para el usuario de prueba
        self.quiz_usuario = QuizUsuario.objects.create(
            usuario=self.user,
            puntaje_total=0,
            cantidad_preguntas=0
        )

    def test_crear_intentos(self):
        # Crear un intento para la pregunta de prueba
        self.quiz_usuario.crear_intentos(pregunta=self.pregunta)
        intentos = PreguntasRespondidas.objects.filter(quizUser=self.quiz_usuario)

        self.assertEqual(intentos.count(), 1)
        self.assertEqual(intentos[0].pregunta, self.pregunta)

    def test_obtener_nuevas_preguntas(self):
        # Obtener nuevas preguntas para el QuizUsuario
        nuevas_preguntas = self.quiz_usuario.obtener_nuevas_preguntas(cantidad_preguntas=5)

        self.assertEqual(nuevas_preguntas.count(), 1)
        self.assertEqual(nuevas_preguntas[0], self.pregunta)

    def test_validar_intento_respuesta_correcta(self):
        # Crear un intento para la pregunta de prueba
        intento = PreguntasRespondidas.objects.create(
            quizUser=self.quiz_usuario,
            pregunta=self.pregunta,
            respuesta=self.respuesta1,
            correcta=False,
            puntaje_obtenido=0
        )

        # Validar el intento con la respuesta correcta
        self.quiz_usuario.validar_intento(pregunta_respondida=intento, respuesta_seleccionada=self.respuesta1)

        intento.refresh_from_db()
        self.assertTrue(intento.correcta)
        self.assertEqual(intento.puntaje_obtenido, self.pregunta.max_puntaje)

    def test_validar_intento_respuesta_incorrecta(self):
        # Crear un intento para la pregunta de prueba
        intento = PreguntasRespondidas.objects.create(
            quizUser=self.quiz_usuario,
            pregunta=self.pregunta,
            respuesta=self.respuesta2,
            correcta=False,
            puntaje_obtenido=0
        )

        # Validar el intento con una respuesta incorrecta
        self.quiz_usuario.validar_intento(pregunta_respondida=intento, respuesta_seleccionada=self.respuesta2)

        intento.refresh_from_db()
        self.assertFalse(intento.correcta)
        self.assertEqual(intento.puntaje_obtenido, 0)

    def test_actualizar_puntaje(self):
        # Crear intentos para preguntas con respuestas correctas
        intento1 = PreguntasRespondidas.objects.create(
            quizUser=self.quiz_usuario,
            pregunta=self.pregunta,
            respuesta=self.respuesta1,
            correcta=True,
            puntaje_obtenido=self.pregunta.max_puntaje
        )
        intento2 = PreguntasRespondidas.objects.create(
            quizUser=self.quiz_usuario,
            pregunta=self.pregunta,
            respuesta=self.respuesta3,
            correcta=True,
            puntaje_obtenido=self.pregunta.max_puntaje
        )

        # Actualizar el puntaje total del QuizUsuario
        self.quiz_usuario.actualizar_puntaje()

        self.assertEqual(self.quiz_usuario.puntaje_total, self.pregunta.max_puntaje * 2)

