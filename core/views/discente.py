from rest_framework.viewsets import ModelViewSet

from core.models import Discente
from core.serializers import DiscenteSerializer

class DiscenteViewSet(ModelViewSet):
    queryset = Discente.objects.all()
    serializer_class = DiscenteSerializer