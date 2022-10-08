from django.db import models

from mind_palace.palace.node.enums import NodeBodyTypeEnum


class NodeBody(models.Model):

    node = models.OneToOneField(
        'node.PalaceNode',
        on_delete=models.CASCADE,
        related_name='body'
    )
    type = models.CharField(
        max_length=50,
        choices=NodeBodyTypeEnum.choices(),
        default=NodeBodyTypeEnum.TEXT
    )
    meta = models.JSONField(default=dict)
    data = models.JSONField(default=dict)
