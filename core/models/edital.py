from tabnanny import verbose
from django.db import models

class Edital(models.Model):
    class Meta:
        verbose_name_plural = "editais"
    
    titulo_longo = models.CharField(max_length=255)
    titulo_curto = models.CharField(max_length=16)
    vigente = models.BooleanField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo_longo