# website/urls.py

from django.conf.urls import url
from django.shortcuts import get_list_or_404

from .models import Page

from . import views

app_name = "website"

urlpatterns = [
	# ex: /
    url(r'^$', views.index, name='index'),
    # ex: /projects/4
    url(r'^projects/(?P<pk>[0-9]+)/', views.projectPage, name="projectPage"),
    # ex: /projects/
    url(r'^projects/', views.projects, name="projects"),
    # /Blog/
    url(r'^blog/$', views.blog, name="blog"),
    # /Blog/4/
    url(r'^blog/(?P<pk>[0-9]+)/', views.blogEntry, name="blogEntry"),
    # /about/
    url(r'^about/', views.about, name="about"),
    # /about/
    url(r'^about', views.about)

]