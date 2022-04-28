from django.db import models

class Edital(models.Model):
    titulo_longo = models.CharField(max_length=255)
    titulo_curto = models.CharField(max_length=16)
    vigente = models.BooleanField()
    url = models.URLField()

    def __str__(self):
        return self.titulo_longo