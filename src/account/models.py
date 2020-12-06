import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        'email address', blank=False, null=False, unique=True,
    )

    # @property
    # def active_avatar(self) -> str:
    #     """
    #     :return: user active avatar url if exists
    #     """
    #     avatar = self.avatar_set.filter(is_active=True).last()
    #     if avatar:
    #         return avatar.file_path.url
    #     return ''

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = str(uuid.uuid4())
        super().save(*args, **kwargs)


def user_avatar_upload(instance, filename):
    return f'{instance.user_id}/{filename}'


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to=user_avatar_upload)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Id: {self.id}, is_active: ' \
               f'{self.is_active}, user: {self.user_id}'

    def save(self, *args, **kwargs):

        if not self.is_active and \
            not self.__class__.objects.filter(user_id=self.user_id).exists():
            self.is_active = True

        if self.is_active:
            self.__class__.objects\
                .filter(user_id=self.user_id)\
                .update(is_active=False)

        super().save(*args, **kwargs)

    # def save(self):
    # self.id - in db
    # not self.id - not in db
    #     pass

    def delete(self, using=None, keep_parents=False):
        # TODO remove file from system
        super().delete(using=using, keep_parents=keep_parents)
