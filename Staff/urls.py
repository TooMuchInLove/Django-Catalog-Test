from django.urls import path
from . import views


routes = (
    '',
    'users/',
    'users_info/',
    'users/user_<int:id>/',
)


urlpatterns = [
    path(routes[0], views.home, name='page-home'),
    path(routes[1], views.get_list_users, name='page-users'),
    path(routes[2], views.get_list_users_info, name='page-users-info'),
    path(routes[3], views.get_info_user, name='page-user-info'),
]
