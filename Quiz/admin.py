from django.contrib import admin

from .models import Pregunta, ElegirRespuesta, Quiz, QuizUsuario, PreguntasRespondidas, QuizSesion

class ElegirRespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    extra = 4

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [ElegirRespuestaInline]

class QuizSesionInline(admin.TabularInline):
    model = QuizSesion

class QuizUsuarioAdmin(admin.ModelAdmin):
    inlines = [QuizSesionInline]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Quiz)
admin.site.register(QuizUsuario, QuizUsuarioAdmin)
admin.site.register(PreguntasRespondidas)
admin.site.register(QuizSesion)
