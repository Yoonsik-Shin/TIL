from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account_update/', views.account_update, name='account_update'),
    path('account_detail/<int:user_pk>/', views.account_detail, name='account_detail'),
]