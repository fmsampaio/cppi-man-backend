from rest_framework import serializers

from core.models import Discente
from .bolsista import BolsistaSerializer

class DiscenteSerializer(serializers.ModelSerializer):
    atuacoes_bolsista = BolsistaSerializer(many=True)

    class Meta:
        model = Discente
        fields = '__all__'
        depth = 3