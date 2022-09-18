from django.db.models import Manager

from .models import Body


class NodeManager(Manager):

    def create(self, body_data: dict = None, **field_values):
        node = super().create(**field_values)
        if body_data:
            Body.objects.create(node=node, **body_data)
        return node
