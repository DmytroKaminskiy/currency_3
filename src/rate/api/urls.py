from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter

app_name = 'api-rate'

router = DefaultRouter()
router.register('rates', views.RateAPIViewSet, basename='rate')

urlpatterns = [
    path('latest/', views.LatestRatesApiView.as_view(), name='latest-rates'),
]

urlpatterns.extend(router.urls)
