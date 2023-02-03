from django.urls import path
from . import views


urlpatterns = [
    # Отображение информации
    path('', views.home, name='page-home'),
    path('users/', views.get_list_users, name='page-users'),
    path('users_info/', views.get_list_users_info, name='page-users-info'),
    path('users/user_<int:id>/', views.get_info_user, name='page-user-info'),
    # Действия пользователя на сайте
    path('login/', views.login_user, name='page-login'),
    # path('logout/', views.logout_user, name='page-logout'),
]
