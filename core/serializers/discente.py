from rest_framework import serializers

from core.models import Discente

class DiscenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discente
        fields = '__all__'