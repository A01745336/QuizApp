from django.contrib import admin

from .models import Pregunta, ElegirRespuesta, Quiz, QuizUsuario, PreguntasRespondidas

class ElegirRespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    extra = 4

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [ElegirRespuestaInline]

class QuizInline(admin.TabularInline):
    model = QuizUsuario.quizes.through

class QuizUsuarioAdmin(admin.ModelAdmin):
    inlines = [QuizInline]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Quiz)
admin.site.register(QuizUsuario, QuizUsuarioAdmin)
admin.site.register(PreguntasRespondidas)
