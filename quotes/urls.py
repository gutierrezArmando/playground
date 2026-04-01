#quotes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path('<int:dia>', views.parametro_int),
    path('<str:dia>', views.parametro_str, name="dia-frase")
]
