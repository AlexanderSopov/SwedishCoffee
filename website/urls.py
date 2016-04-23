# website/urls.py

from django.conf.urls import url
from django.shortcuts import get_list_or_404

from .models import Page

from . import views

app_name = "website"

urlpatterns = [
	# ex: /
    url(r'^$', views.index, name='index'),
    # ex: /projects/
    url(r'^projects/', views.projects, name="projects"),
    # ex: /about/
    url(r'^', views.index, name="about"),
    # /Blog/
    url(r'^ppr/', views.index, name="ppr"),
    # /Blog/
    url(r'^blog/', views.index, name="blog"),
    # /Blog/
    url(r'^dumbit/', views.index, name="dumbit"),
    # /Blog/
    url(r'^lastrafik/', views.index, name="lastrafik"),
    # /Blog/
    url(r'^stub/', views.index, name="stub")
]