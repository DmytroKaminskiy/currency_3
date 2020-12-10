from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rate.api.serializers import RateSerializer
from rate.models import Rate
from rate.selectors import get_latest_rates


class RateAPIViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-id')
    serializer_class = RateSerializer


class LatestRatesApiView(generics.GenericAPIView):
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get(self, request):
        rates = get_latest_rates()
        serializer = RateSerializer(rates, many=True)
        return Response(serializer.data)
