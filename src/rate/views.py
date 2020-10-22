import csv
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView, CreateView
from rate.models import Rate, ContactUs
from django.urls import reverse_lazy
from django.views.generic import View
from rate import choices
from rate.selectors import get_latest_rates

from rate.utils import display


class RateListView(ListView):
    queryset = Rate.objects.all()

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object_count'] = context['object_list'].count()
        return context


class CreateContactUsView(CreateView):
    success_url = reverse_lazy('index')
    model = ContactUs
    fields = ('email', 'subject', 'message')

    def form_valid(self, form):
        # TODO send message
        return super().form_valid(form)


class CSVView(View):
    headers = [
        'sale', 'buy',
        'source', 'currency',
    ]

    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        writer = csv.writer(response)

        from time import sleep

        sleep(15)

        writer.writerow(self.headers)

        for rate in Rate.objects.all().iterator():
            writer.writerow(
                [display(rate, header)
                 for header in self.__class__.headers]
            )

        return response


class LatestRates(View):
    def get(self, request):
        context = {'rate_list': get_latest_rates()}
        return render(request, 'rate/latest-rates.html', context=context)
