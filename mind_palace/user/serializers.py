from djoser.serializers import (
    UserCreateSerializer as DjoserUserCreateSerializer
)
from rest_framework import serializers

from . import models


class UserCreateSerializer(DjoserUserCreateSerializer):

    class Meta(DjoserUserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):

    mind_palace = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.User
        exclude = ('password', )


