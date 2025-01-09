from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/create', views.create_blog, name='create_blog'),
    path('subscribe/', views.subscribe, name='subscribe')


]