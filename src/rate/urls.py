from django.urls import path
from rate import views

from django.views.decorators.cache import cache_page

app_name = 'rate'

urlpatterns = [
    path('list/', cache_page(60)(views.RateListView.as_view()), name='list'),
    # path('list/', views.RateListView.as_view(), name='list'),
    path('list/lastest/', views.LatestRates.as_view(), name='list-latest'),
    path('list/csv/', views.CSVView.as_view(), name='list-csv'),

    path('contact-us/create/', views.CreateContactUsView.as_view(), name='contact-us-create'),
]
