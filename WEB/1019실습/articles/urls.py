from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    path('create/', views.create, name='create'),
    path('comments_create/<int:article_pk>/', views.comments_create, name='comments_create'),
    path('comments_delete/<int:article_pk>/<int:comment_pk>', views.comments_delete, name='comments_delete'),
]