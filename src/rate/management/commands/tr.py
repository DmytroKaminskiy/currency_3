from django.core.management.base import BaseCommand
import random

from django.db import transaction

from rate.models import Rate


class Command(BaseCommand):

    def handle(self, *args, **options):

        with transaction.atomic():
            Rate.objects.create(
                currency=1,
                source=1,
                buy=random.randint(20, 30),
                sale=random.randint(20, 30),
            )
            Rate.objects.create(
                currency=2,
                source=1,
                buy=random.randint(20, 30),
                sale=random.randint(20, 30),
            )
