from django.urls import path

from exam_project.comments.views import CommentsView

urlpatterns = (
    path('', CommentsView.as_view(), name="comments"),
)
