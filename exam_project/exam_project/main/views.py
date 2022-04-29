from functools import reduce

from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.db.models import Q

from exam_project.accounts.models import UserProfile
from exam_project.utils.view_mixins import RedirectIfAuthenticatedMixin

PROFILE = UserProfile


class GreetView(RedirectIfAuthenticatedMixin, views.TemplateView):
    template_name = 'main/greet.html'


class AboutView(views.TemplateView):
    template_name = 'main/about.html'


class IndexView(views.TemplateView):
    template_name = 'main/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('greet'))


class SettingsView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'main/settings.html'


class SearchView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = PROFILE
    template_name = 'main/search.html'

    def get_queryset(self):
        query = self.request.GET['search']
        # Do a search in User DB to filter by email as well?
        filters = Q(first_name=query, last_name=query, alias=query, _connector=Q.OR)
        if query:
            return PROFILE.objects.filter(filters)
        else:
            return None
