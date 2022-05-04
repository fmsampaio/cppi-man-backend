from django.db import models

from core.models import Projeto

class Auxilio(models.Model):
    projeto = models.ForeignKey(
        Projeto,
        related_name="auxilios",
        on_delete=models.CASCADE
    )
    custeio_solicitado = models.FloatField(default=0)
    custeio_contemplado = models.FloatField(default=0)
    custeio_executado = models.FloatField(default=0)
    capital_solicitado = models.FloatField(default=0)
    capital_contemplado = models.FloatField(default=0)
    capital_executado = models.FloatField(default=0)
    url_solicitacao = models.URLField(default=0)

    def __str__(self):
        return f'Aux. Projeto [{self.projeto.titulo}]'
