from core.abstract.views import AbstractViewSet
from .models import User
from .serializers import UserSerializer

class UserViewSet(AbstractViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
