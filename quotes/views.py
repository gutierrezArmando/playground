from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound



#Método que recibe un parametro
def multiDia(request, dia):
    text= None;
    if dia == "lunes":
        text = "Este es el primer día"
    elif dia == "martes":
        text = "Este es el segundo día"
    else:
        return HttpResponseNotFound("Página no encontrada")
    return HttpResponse(text)