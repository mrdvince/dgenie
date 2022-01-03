from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """User model.

    Args:
        AbstractUser: Abstract base class for user models
    """
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)