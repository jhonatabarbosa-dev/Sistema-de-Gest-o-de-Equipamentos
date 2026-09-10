from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    numero_patrimonio = models.IntegerField()
    tipo = models.CharField(max_length=50)
    em_uso = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.numero_patrimonio}"