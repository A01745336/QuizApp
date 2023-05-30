from django.contrib import admin

from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUsuario

from .forms import ElegirInlineFormset


class ElegirRespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.MAXIMO_RESPUESTA
    min_num = ElegirRespuesta.MAXIMO_RESPUESTA
    formset = ElegirInlineFormset



class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInline, )
    list_display = ['texto',]
    search_fields = ['texto', 'preguntas__texto']

class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

    class Meta:
        model = PreguntasRespondidas


@admin.register(QuizUsuario)
class QuizUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'puntaje_total']
    search_fields = ['usuario__username']
    actions = ['generar_preguntas']

    def generar_preguntas(self, request, queryset):
        cantidad_preguntas = int(input("Ingrese la cantidad de preguntas que desea generar: "))
        for quiz_user in queryset:
            preguntas = quiz_user.obtener_nuevas_preguntas(cantidad_preguntas)
            if preguntas:
                for pregunta in preguntas:
                    quiz_user.crear_intentos(pregunta)

    generar_preguntas.short_description = "Generar preguntas para los usuarios seleccionados"


admin.site.register(PreguntasRespondidas, PreguntasRespondidasAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
