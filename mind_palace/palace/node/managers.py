from django.db.models import Manager

from .models import NodeBody


class NodeManager(Manager):

    def create(self, body_data: dict = None, **field_values):
        node = super().create(**field_values)
        if body_data:
            NodeBody.objects.create(node=node, **body_data)
        return node
