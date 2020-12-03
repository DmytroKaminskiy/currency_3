from django.db import models
from rate import choices
from django.core.cache import cache



class Rate(models.Model):
    currency = models.PositiveSmallIntegerField(choices=choices.CURRENCY_CHOICES, db_index=True)
    source = models.PositiveSmallIntegerField(choices=choices.SOURCE_CHOICES)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = (
            ('currency', 'source'),
        )

        permissions = [
            ("full_edit", "This permission allows user to update all available fields in Rate model"),
        ]

    # def __str__(self):
    # TODO FK
    #     return f'{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        key = self.__class__.cache_key(self.currency, self.source)
        cache.delete(key)

    @classmethod
    def cache_key(cls, currency, source) -> str:
        return 'key'
        # import hashlib
        # return hashlib\
        #     .md5(f"RateLatestKey:{currency}_{source}".encode())\
        #     .hexdigest()


class ContactUs(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()
