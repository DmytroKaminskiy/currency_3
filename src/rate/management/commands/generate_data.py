from django.core.management.base import BaseCommand
import random

from rate.models import Rate


class Command(BaseCommand):

    def handle(self, *args, **options):
        rates = []
        for r in range(10_000):
            currency = random.choice([1, 2])
            source = random.choice([1, 2, 3])
            rates.append(
                Rate(
                    currency=currency,
                    source=source,
                    buy=random.randint(20, 30),
                    sale=random.randint(20, 30),
                )
            )

        Rate.objects.bulk_create(rates)
