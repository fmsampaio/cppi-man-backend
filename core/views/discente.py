from rest_framework.viewsets import ModelViewSet

from core.models import Discente
from core.serializers import DiscenteSerializer
from core.serializers.discente import CriarEditarDiscenteSerializer

class DiscenteViewSet(ModelViewSet):
    queryset = Discente.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DiscenteSerializer
        else:
            return CriarEditarDiscenteSerializer