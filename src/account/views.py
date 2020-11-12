from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, View
from account.models import User
from account.forms import UserRegistrationForm

from django.contrib.auth.mixins import LoginRequiredMixin


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy('index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)
        # WRONG return queryset.get(id=self.request.user.id)

# class MyProfile(LoginRequiredMixin, UpdateView):
#     fields = ('first_name', 'last_name')
#     success_url = reverse_lazy('index')
#
#     def get_object(self, queryset=None):
#         return self.request.user


class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    # def form_valid(self, form):
    #     send_sign_up_email.delay(form.instance)
    #     return super().form_valid(form)

    # def get_success_url(self):
        # send_sign_up_email.delay()
        # return super().get_success_url()

class ActivateUser(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        if user.is_active:
            pass
        else:
            user.is_active = True
            user.save(update_fields=('is_active', ))
        return redirect('index')
