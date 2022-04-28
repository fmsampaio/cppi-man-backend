from rest_framework.serializers import ModelSerializer

from core.models import Bolsista

class BolsistaSerializer(ModelSerializer):
    class Meta:
        model = Bolsista
        fields = '__all__'