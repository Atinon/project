from django.urls import path

from exam_project.main.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index page'),
)
