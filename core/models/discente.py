from django.db import models

class Discente(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=16, blank=True)
    matricula = models.CharField(max_length=16, blank=True)
    email = models.EmailField()
    municipio = models.CharField(max_length=64, blank=True)
    telefone = models.CharField(max_length=16, blank=True)
    campus = models.CharField(max_length=32)
    curso = models.CharField(max_length=64)
    link_lattes = models.URLField(blank=True)

    def __str__(self):
        return self.nome