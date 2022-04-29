from rest_framework import serializers

from core.models import Servidor, Edital
from .projeto import SimpleProjetoSerializer

class ServidorSerializer(serializers.ModelSerializer):
    projetos_coordenador = SimpleProjetoSerializer(many=True)

    class Meta:
        model = Servidor
        fields = '__all__'