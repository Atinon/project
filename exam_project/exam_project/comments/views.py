from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from exam_project.accounts.models import UserProfile
from exam_project.comments.forms import CommentsForm
from exam_project.comments.models import ProfileComments

PROFILE_MODEL = UserProfile


class CommentsView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = ProfileComments
    template_name = 'comments/comments_view.html'
    paginate_by = 5
    # ordering = ['-created_on']

    def get_queryset(self):
        receiver = PROFILE_MODEL.objects.get(pk=self.kwargs['pk'])
        if receiver:
            return self.model.objects.filter(receiver=receiver).order_by('-created_on')
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        receiver = PROFILE_MODEL.objects.get(pk=self.kwargs['pk'])
        if receiver:
            context.update({
                'receiver': receiver
            })
        return context


class CreateCommentView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = CommentsForm
    template_name = 'comments/post_comment.html'

    @staticmethod
    def get_profile_model_by_pk(pk):
        return PROFILE_MODEL.objects.get(pk=pk)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['author'] = self.request.user.userprofile
        kwargs['receiver'] = self.get_profile_model_by_pk(self.kwargs['pk'])
        return kwargs

    def get_success_url(self):
        return reverse_lazy('comments', kwargs={'pk': self.kwargs['pk']})
