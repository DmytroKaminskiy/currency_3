import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        'email address', blank=False, null=False, unique=True)

    @property
    def active_avatar(self) -> str:
        """
        TODO
        :return: user active avatar url if exists
        """

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = str(uuid.uuid4())
        super().save(*args, **kwargs)


def user_avatar_upload(instance, filename):
    return f'{instance.user_id}/{filename}'


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to=user_avatar_upload)
    is_active = bool

    # def save(self):
    # self.id - in db
    # not self.id - not in db
    #     pass

    def delete(self, using=None, keep_parents=False):
        # TODO remove file from system
        super().delete(using=None, keep_parents=False)
