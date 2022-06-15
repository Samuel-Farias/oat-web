from django.db import models

# Create your models here.
class Enfermeiro(models.Model):
    Nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    CRE = models.CharField(max_length=100) 
    Endereço = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=100)
def __str__(self):
    return self.nome