from functools import reduce

from django.shortcuts import render
from django.views import generic as views
from django.db.models import Q

from exam_project.accounts.models import UserProfile

PROFILE = UserProfile


# USER = get_user_model()

class IndexView(views.TemplateView):
    template_name = 'main/index.html'


class SettingsView(views.TemplateView):
    template_name = 'main/settings.html'


class SearchView(views.ListView):
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
