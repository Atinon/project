from django.urls import path

from exam_project.accounts.views import UserRegisterView, UserLoginView, ProfileDetailsView, UserLogoutView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('logout/', UserLogoutView.as_view(), name='logout page'),
)
