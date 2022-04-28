from django.db import models

from core.models.servidor import Servidor

class Projeto(models.Model):
    titulo = models.CharField(max_length=256)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    url_projeto = models.URLField(blank=True)
    resumo = models.CharField(max_length=2048, blank=True)
    coordenador = models.ForeignKey(
        Servidor,
        on_delete=models.PROTECT,
        related_name="projetos_coordenador"
        )
    def __str__(self):
        return f'{self.titulo} - {self.coordenador.nome}'