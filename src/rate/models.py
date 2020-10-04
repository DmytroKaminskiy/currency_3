from django.db import models
from rate import choices



class Rate(models.Model):
    currency = models.PositiveSmallIntegerField(choices=choices.CURRENCY_CHOICES)
    source = models.PositiveSmallIntegerField(choices=choices.SOURCE_CHOICES)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()