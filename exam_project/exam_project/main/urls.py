from django.urls import path

from exam_project.main.views import IndexView, SettingsView, SearchView, GreetView, AboutView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('greet/', GreetView.as_view(), name='greet'),
    path('about/', AboutView.as_view(), name='about'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('search_results/', SearchView.as_view(), name='search'),
)
