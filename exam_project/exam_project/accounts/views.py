from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam_project.accounts.forms import CreateProfileForm
from exam_project.accounts.models import UserProfile
from exam_project.utils.view_mixins import RedirectIfAuthenticatedMixin

PROFILE = UserProfile


class UserRegisterView(RedirectIfAuthenticatedMixin, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index')


class UserLoginView(RedirectIfAuthenticatedMixin, auth_views.LoginView):
    template_name = 'accounts/user_login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = PROFILE
    template_name = 'accounts/profile_details.html'

    # checking out url
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.object.picture.url)
        return super().get(request, *args, **kwargs)
