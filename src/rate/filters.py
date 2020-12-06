import django_filters
from django.forms import DateInput

from rate.models import Rate


class RateFilter(django_filters.FilterSet):
    created = django_filters.DateFilter(
        field_name='created', lookup_expr='date',
        widget=DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = Rate
        # fields = ['source', 'currency', 'sale']
        fields = {
            'source': ['exact'],
            'currency': ['exact'],
            'sale': ['exact'],
            'created': [],
        }
