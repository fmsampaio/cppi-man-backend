from django.db import models

class Servidor(models.Model):
    class Meta:
        verbose_name_plural = "servidores"
    
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=16, blank=True)
    siape = models.CharField(max_length=16, blank=True)
    email = models.EmailField()
    campus = models.CharField(max_length=32)
    area_qualis = models.CharField(max_length=64, blank=True)
    link_lattes = models.URLField(blank=True)

    def __str__(self):
        return self.nome