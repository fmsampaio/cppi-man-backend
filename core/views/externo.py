from rest_framework.viewsets import ModelViewSet

from core.models import Externo
from core.serializers import ExternoSerializer

class ExternoViewSet(ModelViewSet):
    queryset = Externo.objects.all()
    serializer_class = ExternoSerializer