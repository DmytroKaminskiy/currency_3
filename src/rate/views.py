from django.views.generic import ListView, CreateView
from rate.models import Rate, ContactUs
from django.urls import reverse_lazy


class RateListView(ListView):
    queryset = Rate.objects.all()


class CreateContactUsView(CreateView):
    success_url = reverse_lazy('index')
    model = ContactUs
    fields = ('email', 'subject', 'message')

    def form_valid(self, form):
        # TODO send message
        return super().form_valid(form)
