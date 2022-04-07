from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam_project.accounts.forms import CreateProfileForm
from exam_project.accounts.models import UserProfile


class UserRegisterView(views.CreateView):
    # model = UserProfile
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index page')
