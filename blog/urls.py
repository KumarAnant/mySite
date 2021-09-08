from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.welcome, name = 'welcomePage'),
    path('posts', views.posts, name = 'postsPage'),
    path('posts/<slug:slug>', views.postDetail, name = 'postDetailsPage')
]
