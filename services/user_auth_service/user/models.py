from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
