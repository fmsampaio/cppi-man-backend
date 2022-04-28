from rest_framework.viewsets import ModelViewSet

from core.models import Bolsista
from core.serializers import BolsistaSerializer

class BolsistaViewSet(ModelViewSet):
    queryset = Bolsista.objects.all()
    serializer_class = BolsistaSerializer