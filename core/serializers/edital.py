from rest_framework import serializers

from core.models import Edital

class EditalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edital
        fields = '__all__'