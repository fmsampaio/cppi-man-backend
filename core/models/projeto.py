from django.db import models
from .edital import Edital
from .externo import Externo
from .servidor import Servidor

class Projeto(models.Model):
    titulo = models.CharField(max_length=256)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    url_projeto = models.URLField(blank=True)
    resumo = models.CharField(max_length=4096, blank=True)
    edital = models.ForeignKey(
        Edital,
        on_delete=models.CASCADE,
        related_name="projetos"
    )
    coordenador = models.ForeignKey(
        Servidor,
        on_delete=models.PROTECT,
        related_name="projetos_coordenador"
        )
    colaboradores_servidores = models.ManyToManyField(
        Servidor,
        related_name="projetos_colaborador",
        blank=True
    )
    colaboradores_externos = models.ManyToManyField(
        Externo,
        related_name="projetos",
        blank=True
    )

    def __str__(self):
        return f'({self.edital.titulo_curto}) {self.titulo} [{self.coordenador.nome}]'