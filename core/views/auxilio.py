from rest_framework.viewsets import ModelViewSet

from core.models import Auxilio
from core.serializers import AuxilioSerializer

class AuxilioViewSet(ModelViewSet):
    queryset = Auxilio.objects.all()
    serializer_class = AuxilioSerializer