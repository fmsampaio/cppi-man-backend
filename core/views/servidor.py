from rest_framework.viewsets import ModelViewSet

from core.models import Servidor
from core.serializers import ServidorSerializer

class ServidorViewSet(ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer