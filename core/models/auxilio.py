from django.db import models

from core.models import Projeto

class Auxilio(models.Model):
    projeto = models.ForeignKey(
        Projeto,
        related_name="auxilios",
        on_delete=models.CASCADE
    )
    custeio_solicitado = models.FloatField(blank=True, null=True)
    custeio_contemplado = models.FloatField(blank=True, null=True)
    custeio_executado = models.FloatField(blank=True, null=True)
    capital_solicitado = models.FloatField(blank=True, null=True)
    capital_contemplado = models.FloatField(blank=True, null=True)
    capital_executado = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'Aux. Projeto [{self.projeto.titulo}]'
