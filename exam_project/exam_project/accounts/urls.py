from django.urls import path, include

from exam_project.accounts.views import UserRegisterView, UserLoginView, ProfileDetailsView, UserLogoutView, \
    ProfileEditView, UserChangePasswordView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register page'),
    path('login/', UserLoginView.as_view(), name='login page'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('<int:pk>/profile_edit/', ProfileEditView.as_view(), name='profile edit'),
    path('change_password/', UserChangePasswordView.as_view(), name='change password'),
    path('logout/', UserLogoutView.as_view(), name='logout page'),

    path('<int:pk>/comments/', include('exam_project.comments.urls')),  # comments APP
)
