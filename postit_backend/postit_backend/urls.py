from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),  
     path("api/auth/", include("core.auth.urls")),
     path('api/post/', include('post.urls')),
]
