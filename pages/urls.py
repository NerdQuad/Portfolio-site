from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('about/', AboutPageView.as_view(), name='about'), 
    path('projects/', ProjectPageView.as_view(), name='projects'),
    path('archive', ArchiveView.as_view(), name='archive'),
]