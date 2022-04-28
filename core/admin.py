from django.contrib import admin
from core.models.bolsista import Bolsista
from core.models.discente import Discente
from core.models.edital import Edital
from core.models.externo import Externo
from core.models.projeto import Projeto
from core.models.servidor import Servidor

# Register your models here.
admin.site.register(Edital)
admin.site.register(Servidor)
admin.site.register(Discente)
admin.site.register(Externo)
admin.site.register(Projeto)
admin.site.register(Bolsista)