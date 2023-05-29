# AppQuizDjango

AppQuizDjango es una aplicación web de Django que permite a los usuarios realizar cuestionarios en línea.

## Prerrequisitos

Necesitarás tener Python 3.7 o superior y pip instalado en tu sistema.

## Instalación

Primero, clona este repositorio en tu máquina local utilizando `git`:

`git clone https://github.com/<your-username>/AppQuizDjango
`

Despues:

`cd AppQuizDjango`


Para instalar las dependencias necesarias, primero es recomendable crear un entorno virtual para este proyecto. Puedes hacerlo con el siguiente comando en la consola:

`python -m venv quizenv`


Activa el entorno virtual con:

`.\quizenv\Scripts\activate`


Una vez activado el entorno virtual, instala las dependencias con:

`pip install django`


## Inicio del proyecto

Para iniciar el proyecto Django, sigue estos pasos:

1. Navega a la carpeta de tu proyecto, en este caso "AppQuizDjango": ``cd AppQuizDjango``

2. Inicia el proyecto Django con el siguiente comando:
``django-admin startproject quizapp``


3. Navega a la carpeta del proyecto Django recién creado:
``cd quizapp``


4. Inicia la aplicación principal del proyecto:
``py manage.py startapp main``


## Ejecución del servidor

Una vez configurada la aplicación, puedes ejecutar el servidor con el siguiente comando:


``py manage.py runserver``


Esto iniciará el servidor de desarrollo de Django en `http://127.0.0.1:8000/`.

## Pruebas

Para ejecutar las pruebas para este proyecto, navega al directorio del proyecto y ejecuta el siguiente comando:

``python manage.py test``


Esto ejecutará automáticamente todas las pruebas del proyecto.

## Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz fork del repositorio.
2. Crea una nueva rama.
3. Haz tus cambios y escribe pruebas si es posible.
4. Envía una solicitud pull al repositorio original para revisión.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
