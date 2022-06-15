from django.db import models

# Create your models here.
class RH(models.Model):
    Nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    RG = models.CharField(max_length=100)
    Nascimento = models.DateField(max_length=100)
    Cargo = models.CharField(max_length=100)
    Salario = models.FloatField(max_length=100)
    Endereço = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=100)
    CTPS = models.DateField(max_length=100)
def __str__(self):
    return self.nome