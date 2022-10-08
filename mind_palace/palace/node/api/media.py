from rest_framework.viewsets import ModelViewSet

from mind_palace.palace.node.models import NodeMedia
from mind_palace.palace.node.serializers import NodeMediaSerializer


class MindPalaceNodeMediaViewSet(ModelViewSet):

    queryset = NodeMedia.objects.all()
    serializer_class = NodeMediaSerializer
