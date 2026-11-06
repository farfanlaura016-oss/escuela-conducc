from django.shortcuts import render
from .models import ClaseManejo

def lista_clases(request):
    clases = ClaseManejo.objects.all()
    context = {
        'clases': clases,
        'total_clases': clases.count()
    }
    return render(request, 'autoescuela/lista_clases.html', context)