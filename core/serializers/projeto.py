from rest_framework.serializers import ModelSerializer

from core.models.projeto import Projeto

class ProjetoSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'