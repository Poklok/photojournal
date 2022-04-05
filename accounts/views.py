from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import ListView, FormView
from requests import request

from accounts.models import Profile


class ProfilePageView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'


class UserRegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = '../profile'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)