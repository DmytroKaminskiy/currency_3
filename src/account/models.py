import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        'email address', blank=False, null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = str(uuid.uuid4())
        super().save(*args, **kwargs)

# class User(AbstractUser):
#     pass
