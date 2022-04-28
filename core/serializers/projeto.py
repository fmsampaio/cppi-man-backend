from rest_framework.serializers import ModelSerializer

from core.models import Projeto
from .bolsista import BolsistaSerializer

class ProjetoSerializer(ModelSerializer):
    bolsistas = BolsistaSerializer(many=True)
    
    class Meta:
        model = Projeto
        fields = '__all__'
        depth = 1