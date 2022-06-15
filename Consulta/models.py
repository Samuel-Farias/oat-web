from django.db import models

# Create your models here.
class Consulta(models.Model):
    Paciente = models.CharField(max_length=100)
    CPF_Paciente = models.CharField(max_length=100)
    Medico = models.CharField(max_length=100)
    CRM = models.CharField(max_length=100) 
    Data = models.DateField(max_length=100)
    Valor = models.FloatField(max_length=100)
    
def __str__(self):
    return self.nome