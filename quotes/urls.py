from django.urls import path
from . import views

urlpatterns = [
    path('<dia>', views.multiDia)
]
