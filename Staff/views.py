from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Position, User
#
# from .forms import CategoryForm, ToDoListForm


def home(request):
    templates = 'main.html'

    return render(request, templates)

def get_list_users(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    templates = 'users/list_users.html'

    return render(request, templates, context)
