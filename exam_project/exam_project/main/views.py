from django.shortcuts import render
from django.views import generic as views


class IndexView(views.TemplateView):
    template_name = 'main/index.html'
