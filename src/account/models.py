from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        'email address', blank=False, null=False, unique=True)

# class User(AbstractUser):
#     pass
