from django.db import models

class Ativo(models.Model):
    nome = models.CharField(max_length=120)
    codigo = models.CharField(max_length=14, unique=True)
    limite_inferior = models.FloatField()
    limite_superior = models.FloatField()
    periodicidade = models.IntegerField()
    ultima_cotacao = models.FloatField(null=True, blank=True)
    
def __str__(self):
    return f"Ativo: {self.nome}, Código: {self.codigo}"

