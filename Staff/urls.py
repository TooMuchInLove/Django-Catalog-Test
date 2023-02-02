from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='page-home'),
    path('users/', views.get_list_users, name='page-users'),
]
