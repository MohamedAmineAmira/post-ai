from django.db import models
from core.abstract.models import AbstractModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    """Custom manager for User model"""

    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        """Required for Django authentication"""
        return self.get(email=email)


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False)  

    objects = UserManager() 

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def save(self, *args, **kwargs):
        if self._state.adding and self.password:
            self.password = make_password(self.password)  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
