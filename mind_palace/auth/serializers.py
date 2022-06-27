from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from mind_palace.user import serializers as user_serializers


class TokenPairObtainSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['user'] = user_serializers.UserSerializer(self.user).data
        return validated_data


