from django.db import models

#criando a tabela Todo
class Formulario(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=150, null=False, blank=False)
    email = models.EmailField(verbose_name="E-mail", max_length=150, null=False, blank=False)
    dtNasc = models.DateTimeField(verbose_name="Data de Nascimento", null=False, blank=False)
    resp01 = models.CharField(verbose_name="Possui moto?", max_length=150, null=False, blank=False)
    resp02 = models.CharField(verbose_name="Possui carro?", max_length=150, null=False, blank=False)
    resp03 = models.CharField(verbose_name="Possui avião?", max_length=150, null=False, blank=False)


