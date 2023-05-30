from django.contrib import admin
from .models import Pregunta, ElegirRespuesta, Quiz, QuizUsuario, PreguntasRespondidas


class ElegirRespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    extra = 4


class PreguntaAdmin(admin.ModelAdmin):
    inlines = [ElegirRespuestaInline]


class QuizAdmin(admin.ModelAdmin):
    filter_horizontal = ('preguntas',)


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizUsuario)
admin.site.register(PreguntasRespondidas)
admin.site.register(ElegirRespuesta)
