from django.contrib import admin
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUsuario


class ElegirRespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    extra = 4


class PreguntaAdmin(admin.ModelAdmin):
    inlines = [ElegirRespuestaInline]


class PreguntasRespondidasInline(admin.TabularInline):
    model = PreguntasRespondidas
    extra = 1


class QuizUsuarioAdmin(admin.ModelAdmin):
    inlines = [PreguntasRespondidasInline]


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(QuizUsuario, QuizUsuarioAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(PreguntasRespondidas)
