"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from formulario.views import home, lista
from formulario.views import ListarView
from formulario.views import CriarView
from formulario.views import AtualizarView
from formulario.views import DeletarView
from formulario.views import CompletarView
from formulario.views import DetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home),
    #path('', lista),
    path("", ListarView.as_view(template_name="formulario/lista.html"), name='listar'),
    path("criar", CriarView.as_view(), name='criar'),
    # pk é o parametro da tarefa que será atualizada
    path("atualizar/<int:pk>",
         AtualizarView.as_view(), name='atualizar'),
    path("excluir/<int:pk>",
         DeletarView.as_view(), name='excluir'),
    path("completar/<int:pk>",
         CompletarView.as_view(), name='completar'),
    path("print/<int:pk>",
         DetailView.as_view(), name='print'),
    
]
