from functools import reduce

from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.db.models import Q

from exam_project.accounts.models import UserProfile
from exam_project.utils.view_mixins import RedirectIfAuthenticatedMixin
from exam_project.comments.models import ProfileComments

PROFILE = UserProfile
COMMENTS = ProfileComments


class GreetView(RedirectIfAuthenticatedMixin, views.TemplateView):
    template_name = 'main/greet.html'


class AboutView(views.TemplateView):
    template_name = 'main/about.html'


class IndexView(views.ListView):
    template_name = 'main/index.html'

    COMMENTS_COUNT = 20
    ORDER_CRITERION = '-created_on'

    queryset = COMMENTS.objects.order_by(ORDER_CRITERION)[:COMMENTS_COUNT]
    context_object_name = 'recent_comments'
    paginate_by = 10

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
        if query:
            filters = Q(
                first_name__icontains=query,
                last_name__icontains=query,
                alias__icontains=query,
                _connector=Q.OR)
            return PROFILE.objects.filter(filters)
        else:
            return PROFILE.objects.none()
