from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('post/<id>/',views.Post,name='post'),
    path('search',views.search,name="search")
]