from django.core.cache import cache
from rate.models import Rate
from rate import choices

def get_latest_rates():

    ### TO CACHE
    rates = []
    key = Rate.cache_key()

    if key in cache:
        return cache.get(key)
    else:
        for source_int, _ in choices.SOURCE_CHOICES:
            for currency_int, _ in choices.CURRENCY_CHOICES:
                if key in cache:
                    rate = cache.get(key)
                else:
                    # # slow
                    rate = Rate.objects \
                        .filter(source=source_int, currency=currency_int) \
                        .order_by('created') \
                        .last()

                # if rate is not None:
                if rate:
                    rates.append(rate)
        # CACHE

    return rates