from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.refresh import RefreshViewSet

router = DefaultRouter()
router.register(r"register", RegisterViewSet, basename="register")
router.register(r"login", LoginViewSet, basename="login")
router.register(r"refresh", RefreshViewSet, basename="refresh")

urlpatterns = router.urls
