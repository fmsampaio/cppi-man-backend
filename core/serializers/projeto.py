from rest_framework.serializers import ModelSerializer, CharField

from core.models import Projeto
from .bolsista import BolsistaSerializer

class ProjetoSerializer(ModelSerializer):
    bolsistas = BolsistaSerializer(many=True)
    
    class Meta:
        model = Projeto
        fields = '__all__'
        depth = 1

class SimpleProjetoSerializer(ModelSerializer):

    edital = CharField(source='edital.titulo_longo')
    
    class Meta:
        model = Projeto
        fields = ('titulo', 'data_inicio', 'data_termino', 'edital')
    