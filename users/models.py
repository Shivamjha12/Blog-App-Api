from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

class User(AbstractUser):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()