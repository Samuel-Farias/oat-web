from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    Nome = models.CharField(max_length=100)
    CPF_CNPJ = models.CharField(max_length=100) 
    Endereço = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Telefone = models.CharField(max_length=100)
def __str__(self):
    return self.nome