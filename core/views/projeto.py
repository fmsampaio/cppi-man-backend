from rest_framework.viewsets import ModelViewSet

from core.models.projeto import Projeto
from core.serializers.projeto import ProjetoSerializer

class ProjetoViewSet(ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer