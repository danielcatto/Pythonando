from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologias


def nova_empresa(request):
    if request.method == 'GET':
        techs = Tecnologias.objects.all()    
    elif  request.method == 'POST':
        nome = request.POST.get('nome')
        return HttpResponse(nome)
    return render(request, 'nova_empresa.html', {'techs':techs})