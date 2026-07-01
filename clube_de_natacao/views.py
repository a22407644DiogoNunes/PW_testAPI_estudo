from django.shortcuts import render
from .models import * 

# Create your views here.
def nadadores_view(request):
    nadadores = Nadador.objects.all()

    context = {
        'nadadores':nadadores
    }

    return render(request, "clube_de_natacao/nadadores.html", context)
