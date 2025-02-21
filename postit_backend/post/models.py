from django.db import models
from core.abstract.models import AbstractModel
from django.conf import settings

class Post(AbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    context = models.TextField() 
    generated_post = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"Post by {self.user.full_name} - {self.context[:30]}..."
