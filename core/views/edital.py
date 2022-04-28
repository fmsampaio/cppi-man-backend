from rest_framework.viewsets import ModelViewSet

from core.models import Edital
from core.serializers.edital import EditalSerializer

class EditalViewSet(ModelViewSet):
    queryset = Edital.objects.all()
    serializer_class = EditalSerializer