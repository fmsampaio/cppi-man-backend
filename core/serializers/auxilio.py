from rest_framework.serializers import ModelSerializer

from core.models import Auxilio

class AuxilioSerializer(ModelSerializer):
    class Meta:
        model = Auxilio
        fields = '__all__'