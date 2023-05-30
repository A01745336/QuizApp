from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from .forms import RegistroFormulario, UsuarioLoginFormulario
from .models import QuizUsuario, Pregunta, PreguntasRespondidas


def inicio(request):
    context = {
        'bienvenido': 'Welcome'
    }
    return render(request, 'inicio.html', context)


def HomeUsuario(request):
    return render(request, 'Usuario/home.html')


def tablero(request):
    total_usuarios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
    contador = total_usuarios_quiz.count()

    context = {
        'usuario_quiz': total_usuarios_quiz,
        'contar_user': contador
    }

    return render(request, 'play/tablero.html', context)


def jugar(request):
    quiz_user, created = QuizUsuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = quiz_user.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
        except ObjectDoesNotExist:
            raise Http404

        quiz_user.validar_intento(pregunta_respondida, opcion_seleccionada)
        quiz_user.cantidad_preguntas -= 1
        quiz_user.save()

        if quiz_user.intentos.count() < quiz_user.cantidad_preguntas:
            nuevas_preguntas = quiz_user.obtener_nuevas_preguntas(1)
            if nuevas_preguntas:
                quiz_user.crear_intentos(nuevas_preguntas[0])
                pregunta = nuevas_preguntas[0]
            else:
                pregunta = None
        else:
            pregunta = None

        if pregunta is None or quiz_user.cantidad_preguntas == 0:
            # Redirige a la página de resultados si se han respondido todas las preguntas
            return redirect('resultado', pregunta_respondida_pk=pregunta_respondida.pk)
        else:
            # Redirige nuevamente a la vista 'jugar' con la cantidad de preguntas
            return redirect(f'/jugar/?cantidad_preguntas={quiz_user.cantidad_preguntas}')

    else:
        cantidad_preguntas = request.GET.get('cantidad_preguntas')
        if cantidad_preguntas:
            cantidad_preguntas = int(cantidad_preguntas)
        else:
            cantidad_preguntas = 1

        quiz_user.cantidad_preguntas = cantidad_preguntas
        quiz_user.save()

        nuevas_preguntas = quiz_user.obtener_nuevas_preguntas(1)
        if nuevas_preguntas:
            quiz_user.crear_intentos(nuevas_preguntas[0])
            pregunta = nuevas_preguntas[0]
        else:
            pregunta = None

    context = {
        'pregunta': pregunta,
        'cantidad_preguntas': cantidad_preguntas
    }

    return render(request, 'play/jugar.html', context)




def resultado_pregunta(request, pregunta_respondida_pk):
    respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

    context = {
        'respondida': respondida
    }
    return render(request, 'play/resultados.html', context)


def loginView(request):
    titulo = 'login'
    form = UsuarioLoginFormulario(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        usuario = authenticate(username=username, password=password)
        login(request, usuario)
        return redirect('HomeUsuario')

    context = {
        'form': form,
        'titulo': titulo
    }

    return render(request, 'Usuario/login.html', context)


def registro(request):
    titulo = 'Crear una Cuenta'
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroFormulario()

    context = {
        'form': form,
        'titulo': titulo
    }

    return render(request, 'Usuario/registro.html', context)


def logout_vista(request):
    logout(request)
    return redirect('/')
