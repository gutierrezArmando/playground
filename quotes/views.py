#quotes/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

misFrases = {
    "lunes":"Pricio de semana, No voy a trabajar!",
    "martes": "Ni te cases ni te embarques, Pa' que voy a arriesgarme, No voy a trabajar",
    "miercoles":"Se casa la patrona, Ay que pachangona, No voy a trabajar",
    "jueves":"Estoy muy desvelado, Me siento hasta mareado, No voy a trabaja",
    "viernes":"Que muere jesucristo, Donde se ha visto?, No voy a trabajar"
}

def index(request):
    list_frases = ""
    for frase in misFrases:
        path_dia = reverse("dia-frase",args=[frase])
        list_frases +=f'<li><a href="{path_dia}">{frase}</a></li>'
    html_response = f"<ul>{list_frases}</ul>"
    return HttpResponse(html_response)

def parametro_str(request, dia):
    try:
        frase = misFrases[dia]
        return HttpResponse(frase)
    except KeyError:
        return HttpResponseNotFound("Este día no existe")

def parametro_int(request, dia):
    dias = list(misFrases.keys())
    if dia > len(dias):
        return HttpResponseNotFound("El dá no existe")
    redirect_dia = dias[dia-1]
    redirect_path = reverse("dia-frase", args=[redirect_dia])
    return HttpResponseRedirect(redirect_path)


