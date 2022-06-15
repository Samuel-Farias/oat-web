from django.db import models

# Create your models here.
class Convenio(models.Model):
    Nome = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=100)
    Contrato = models.CharField(max_length=100)
    Data_adesão = models.DateField(max_length=100)
    Data_término = models.DateField(max_length=100)
    
def __str__(self):
    return self.nome