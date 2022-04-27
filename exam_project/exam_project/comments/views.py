from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views

from exam_project.comments.models import ProfileComments


class CommentsView(auth_mixins.LoginRequiredMixin,views.ListView):
    model = ProfileComments
    template_name = 'comments/comments_view.html'
