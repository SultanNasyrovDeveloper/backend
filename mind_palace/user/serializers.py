from djoser.serializers import (
    UserCreateSerializer as DjoserUserCreateSerializer
)

from . import models


class UserSerializer(DjoserUserCreateSerializer):

    class Meta(DjoserUserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'password')
