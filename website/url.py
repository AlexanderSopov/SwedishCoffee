from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='website'),
    url(r'^projects/', views.index, name="Projects"),
    url(r'^projects/', views.index, name="About"),
    url(r'^projects/', views.index, name="Blog")
]