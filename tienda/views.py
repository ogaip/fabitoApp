from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'tienda/index.html',
                  {'title': 'Inicio',
                   'message': 'Bienvenido a la tienda de Faabito'})
