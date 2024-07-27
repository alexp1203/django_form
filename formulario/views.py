from django.shortcuts import render
from django.http import HttpResponse
from .models import Formulario
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


def home(request):
    #return HttpResponse('view Home')
    return render(request,'formulario/home.html')

# Create your views here.
#def formLista(request):
 #   return render(request, "formulario/lista.html")

def lista(request):
    registros = Formulario.objects.all()  # busca todos os dados do banco
    return render(request, "formulario/lista.html",{'registros':registros})

class ListarView(ListView):
    model = Formulario

class CriarView(CreateView):
    model = Formulario
    fields = ["nome","data de Nascimento", "e-mail", "Possui moto?", "Possui carro?", "Possui avião?"]

class CriarView(CreateView):
    model = Formulario
    fields = ["nome","dtNasc", "email", "resp01", "resp02", "resp03"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('lista')