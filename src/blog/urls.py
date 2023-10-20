from django.urls import path
from .views import index,article

urlpatterns= [
    path('', index, name="blog-index"),
    path('article-<str:num_art>/',article,name="blog-article"),


]