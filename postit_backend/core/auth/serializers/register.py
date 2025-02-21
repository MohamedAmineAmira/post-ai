from rest_framework import serializers
from user.models import User
from user.serializers import UserSerializer

class RegisterSerializer(UserSerializer):
    """Serializer for user registration"""

    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model = User
        fields = ["id", "full_name", "email", "password"]

    def create(self, validated_data):
        return User.objects.create(**validated_data)
