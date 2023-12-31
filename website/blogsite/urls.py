
from django.urls import  path
from . import views
from .views import ArticleDetailView, AddPostView, DeletePostView, UpdatePostView, HomeView, my_articles

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('article/', my_articles, name='post'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='addpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),name="update"),
    path('article/<int:pk>/remove', DeletePostView.as_view(),name="delete"),
     path('submit/', views.submit_url, name='submit_url'),
    path('urls/', views.url_list, name='url_list'),
]