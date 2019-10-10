from django.urls import path, include
from . import views
import re


app_name="blog"
urlpatterns=[
    path('', views.IndexView.as_view(), name="index"),
    #path('<int:post_id>/',views.detail, name='post'),
    path('<int:pk>/',views.DetailView.as_view(), name='post'),
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('<int:post_id>/deletePost/', views.delete_post, name='delete_post'),
    path('add_post/',views.addPostView.as_view(),name="add_post"),
    path('search', views.searchList.as_view(), name="search_list")

]
