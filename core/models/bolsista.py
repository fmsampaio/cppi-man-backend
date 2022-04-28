from django.db import models
from core.models.discente import Discente

from core.models.projeto import Projeto

class Bolsista(models.Model):
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="bolsistas"
    )
    discente = models.ForeignKey(
        Discente,
        on_delete=models.CASCADE,
        related_name="atuacoes_bolsista"
    )
    data_inicio = models.DateField()
    data_termino = models.DateField()
    modalidade = models.CharField(max_length=16)
    carga_horaria = models.IntegerField()
    valor_bolsa = models.FloatField()
    banco = models.CharField(max_length=32, blank=True)
    agencia_banco = models.CharField(max_length=16, blank=True)
    conta_banco = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return f'[{self.modalidade} - {self.carga_horaria}h] ({self.data_inicio} - {self.data_termino}) {self.projeto.titulo}'