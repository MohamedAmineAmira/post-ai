from core.abstract.serializers import AbstractSerializer
from user.models import User  

class UserSerializer(AbstractSerializer):
    class Meta(AbstractSerializer.Meta):
        model = User
        fields = AbstractSerializer.Meta.fields + ["full_name", "email", "password","is_active"]
        extra_kwargs = {"password": {"write_only": True}}  # Prevent password from being returned
