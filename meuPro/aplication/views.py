from django.views.generic.edit import CreateView
from django.shortcuts import render
from aplication.models import Items
from django.urls import reverse_lazy


# Create your views here.

# aqui eu fiz uma viw generica
class Create(CreateView):
    model = Items
    fields = ['nome', 'email', 'assunto', 'mensagem']
    template_name = 'aplication/contato.html'
    success_url = reverse_lazy('contato')


def index(request):
    return render(request, template_name='aplication/index.html')


def moda(request):
    return render(request, template_name='aplication/moda.html')


def beleza(request):
    return render(request, template_name='aplication/beleza.html')


def tendencia(request):
    return render(request, template_name='aplication/tendencia.html')


def contato(request):
    return render(request, template_name='aplication/contato.html')
