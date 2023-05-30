from django.contrib import admin

from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUsuario, Quiz

from .forms import ElegirInlineFormset


class ElegirRespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.MAXIMO_RESPUESTA
    min_num = ElegirRespuesta.MAXIMO_RESPUESTA
    formset = ElegirInlineFormset


class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInline,)
    list_display = ['texto', ]
    search_fields = ['texto', 'preguntas__texto']


class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']


class QuizInline(admin.StackedInline):
    model = Quiz
    extra = 0


class QuizUsuarioAdmin(admin.ModelAdmin):
    inlines = [QuizInline]


admin.site.register(PreguntasRespondidas, PreguntasRespondidasAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(QuizUsuario, QuizUsuarioAdmin)
admin.site.register(Quiz)
