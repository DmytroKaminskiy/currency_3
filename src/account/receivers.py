from django.db.models.signals import post_delete
from django.dispatch import receiver

from account.models import Avatar


@receiver(post_delete, sender=Avatar)
def avatar_post_delete_remove_avatar(sender, instance, *args, **kwargs):
    instance.file_path.delete()
