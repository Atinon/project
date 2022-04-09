from django.urls import path

from exam_project.main.views import IndexView, SettingsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('settings/', SettingsView.as_view(), name='settings'),
)
