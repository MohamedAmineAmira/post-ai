from rest_framework import serializers
from post.models import Post
from core.abstract.serializers import AbstractSerializer


class PostSerializer(AbstractSerializer):
    generated_post = serializers.CharField(read_only=True)  

    class Meta:
        model = Post
        fields = ["public_id", "user", "context", "generated_post"]
        extra_kwargs = {"user": {"read_only": True}}  # User is set automatically from JWT
