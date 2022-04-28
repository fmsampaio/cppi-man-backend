from django.contrib import admin

from core.models.edital import Edital
from core.models.servidor import Servidor

# Register your models here.
admin.site.register(Edital)
admin.site.register(Servidor)