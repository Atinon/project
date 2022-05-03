from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from exam_project.accounts.forms import CreateProfileForm, ProfileEditForm
from exam_project.accounts.models import UserProfile, ProjectUser
from exam_project.utils.view_mixins import RedirectIfAuthenticatedMixin

USER = ProjectUser
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


class ProfileEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    form_class = ProfileEditForm
    model = PROFILE
    template_name = 'accounts/profile_edit.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.id != :
    #         return redirect(reverse_lazy('index'))
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'is_owner': self.object.user.id == self.request.user.id,
        }
        )
        return context

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/user_change_password.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Password changed successfully")
        return super().form_valid(form)

    # def get_success_url(self):
    #     object = self.get_object()
    #     return reverse_lazy('profile details', kwargs={'pk': object.pk})


class UserLogoutView(auth_views.LogoutView):
    next_page = 'index'


class UserDeleteView(views.DeleteView):
    model = PROFILE
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('index')