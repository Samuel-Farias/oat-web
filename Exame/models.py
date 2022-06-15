from django.db import models

# Create your models here.
class Exame(models.Model):
    Tipo_Exame = models.CharField(max_length=100)
    Paciente = models.CharField(max_length=100)
    CPF_Paciente = models.CharField(max_length=100)
    Profissional_Responsável = models.CharField(max_length=100)
    CPF_Profissional = models.CharField(max_length=100) 
    Data = models.DateField(max_length=100)
    Valor = models.FloatField(max_length=100)
    
def __str__(self):
    return self.nome