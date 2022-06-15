from django.db import models

# Create your models here.
class Insumo_hospitalar(models.Model):
    Nome = models.CharField(max_length=100)
    Valor_custo = models.FloatField(max_length=100)
    Valor_repasse = models.CharField(max_length=100)
    Vencimento = models.DateField(max_length=100)
    Quantidade = models.CharField(max_length=100)
    Marca = models.FloatField(max_length=100)
def __str__(self):
    return self.nome