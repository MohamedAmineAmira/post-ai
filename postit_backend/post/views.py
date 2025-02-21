from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from post.serializers import PostSerializer
from post.services import generate_social_media_post 
from core.abstract.views import AbstractViewSet
from rest_framework.decorators import action

class PostViewSet(AbstractViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["post", "get", "put", "delete"]

    @action(detail=False, methods=["post"])
    def generate_post(self, request, *args, **kwargs):

        """Create a post with AI-generated content."""
        user = request.user  
        context = request.data.get("context")
        
        if not context:
            return Response(
                {"error": "Context is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Generate post content using OpenAI
            generated_post = generate_social_media_post(context)
            
            if not generated_post:
                return Response(
                    {"error": "Failed to generate post"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # Save post with user field
            post = Post.objects.create(
                user=user,
                context=context,
                generated_post=generated_post
            )
            
            return Response(
                PostSerializer(post).data,
                status=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            return Response(
                {"error": f"Error generating post: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
