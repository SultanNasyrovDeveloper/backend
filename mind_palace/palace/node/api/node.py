from datetime import datetime, timedelta

from django.conf import settings
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from mind_palace.palace.node import models, serializers, filters


class MindPalaceNodeViewSet(viewsets.ModelViewSet):

    queryset = models.PalaceNode.objects.all()
    serializer_class = serializers.MindPalaceNodeSerializer
    filterset_class = filters.MindPalaceNodeFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.NodeBriefInfoSerializer
        return super().get_serializer_class()

    def retrieve(self, request, pk=None, *args, **kwargs):
        node = self.get_object()
        should_update_views_count = (
            node.owner_id == request.user.id
            and datetime.now() > node.last_view + timedelta(
                minutes=settings.UPDATE_NODE_AFTER_MINUTES
            )
        )
        if should_update_views_count:
            node.learning_statistics.views += 1
            node.learning_statistics.last_view = datetime.utcnow()
            node.learning_statistics.save()
        return Response(self.serializer_class(node).data)

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        data['owner'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        if 'body' in request.data:
            raise ValidationError('Node body should be updated through body endpoint.')
        return super().update(request, *args, **kwargs)
