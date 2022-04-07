from django.urls import path

from exam_project.accounts.views import UserRegisterView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register page'),
)
