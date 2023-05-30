
# This code is defining the URL patterns for a Django web application.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Quiz.urls'))
]
