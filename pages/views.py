from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ProjectPageView(TemplateView):
    template_name = 'project.html'


class ArchiveView(TemplateView):
    template_name = 'archive.html'