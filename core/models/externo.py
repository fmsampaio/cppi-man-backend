from django.db import models

class Externo(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=16, blank=True)
    email = models.EmailField()
    instituicao = models.CharField(max_length=32)
    link_lattes = models.URLField(blank=True)

    def __str__(self):
        return self.nome