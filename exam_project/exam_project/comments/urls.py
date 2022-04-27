from django.urls import path

from exam_project.comments.views import CommentsView, CreateCommentView

urlpatterns = (
    path('', CommentsView.as_view(), name="comments"),
    path('test_post/', CreateCommentView.as_view(), name="test post comment"),
)
