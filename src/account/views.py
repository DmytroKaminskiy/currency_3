from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, View, ListView
from account.models import User, Avatar
from account.forms import UserRegistrationForm, AvatarForm

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

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def form_valid(self, form):
    #     send_sign_up_email.delay(form.instance)
    #     return super().form_valid(form)

    # def get_success_url(self):
        # send_sign_up_email.delay()
        # return super().get_success_url()

class CreateUserAvatar(LoginRequiredMixin, CreateView):
    model = Avatar
    form_class = AvatarForm
    success_url = reverse_lazy('index')

    # def get_form(self, form_class=None):
    #     """Return an instance of the form to be used in this view."""
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #     return form_class(request=self.request, **self.get_form_kwargs())
        # return form_class(request=self.request, initial={}, prifix=None, instance=None)

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs


class ActivateUser(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        if user.is_active:
            pass
        else:
            user.is_active = True
            user.save(update_fields=('is_active', ))
        return redirect('index')


class Avatars(LoginRequiredMixin, ListView):
    # queryset = Avatar.objects.all()
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user)

    def get_queryset(self):
        return self.request.user.avatar_set.all()
