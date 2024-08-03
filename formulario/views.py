from django.shortcuts import render
from django.http import HttpResponse
from .models import Formulario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from datetime import date

def home(request):
    #return HttpResponse('view Home')
    return render(request,'formulario\home.html')

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
    fields = ["nome","dtNasc", "email", "resp01", "resp02", "resp03"]
    success_url = reverse_lazy('listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Adicionar Registro'
        return context


class AtualizarView(UpdateView):
    model = Formulario
    fields = ["nome","dtNasc", "email", "resp01", "resp02", "resp03"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Atualizar Registro'
        return context
    
class DeletarView(DeleteView):
    model = Formulario
    success_url = reverse_lazy('listar')
    template_name = "formulario/formulario_confirm_delete.html"

class CompletarView(View):
    def get(self,request,pk):
        registro = Formulario.objects.get(pk=pk)
        registro.save()
        return redirect('listar')
    
class DetailView(DetailView):
    model = Formulario
    fields = ["nome","dtNasc", "email", "resp01", "resp02", "resp03"]
    template_name = 'formulario/formulario/print.html'
    success_url = reverse_lazy('listar')

    def print(request):
        registros = Formulario.objects.all()  # busca todos os dados do banco
        return render(request, "formulario/formulario/print.html",{'registros':registros})
    
