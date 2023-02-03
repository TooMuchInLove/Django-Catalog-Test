from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Position, User
#
# from .forms import CategoryForm, ToDoListForm


def get_sort_data(request):

    users = User.objects.all()

    if request.method == 'POST':
        # Кортеж ключей для запроса
        keys_for_query = (
            'id', '-id', # Сортировка по идентификатору
            'name', '-name', # Сортировка по ФИО
            'date', '-date', # Сортировка по дате приёма на работу
            'amount', '-amount', # Сортировка по з/п
            'fk_position', '-fk_position', # Сортировка по должности
        )
        # Получаем ключ имени кнопки
        value = list(request.POST.keys())[1]
        for item in keys_for_query:
            if item == value:
                if item == 'fk_position' or item == '-fk_position':
                    # 'fk_position__name' -> обращаемся к таблице 'Position' - поле 'name'
                    users = User.objects.all().order_by('%s__name' % (value))
                else:
                    users = User.objects.all().order_by(value)

        # if 'id' in request.POST: # Сортировка по идентификатору
        #     users = User.objects.all().order_by('id')
        # elif '-id' in request.POST:
        #     users = User.objects.all().order_by('-id')
        # elif 'name' in request.POST: # Сортировка по ФИО
        #     users = User.objects.all().order_by('name')
        # elif '-name' in request.POST:
        #     users = User.objects.all().order_by('-name')
        # elif 'date' in request.POST: # Сортировка по дате приёма на работу
        #     users = User.objects.all().order_by('date')
        # elif '-date' in request.POST:
        #     users = User.objects.all().order_by('-date')
        # elif 'amount' in request.POST: # Сортировка по з/п
        #     users = User.objects.all().order_by('amount')
        # elif '-amount' in request.POST:
        #     users = User.objects.all().order_by('-amount')
        # elif 'fk_position' in request.POST: # Сортировка по должности
        #     users = User.objects.all().order_by('fk_position__name')
        # elif '-fk_position' in request.POST:
        #     users = User.objects.all().order_by('-fk_position__name')

    return users

def home(request):
    templates = 'main.html'

    return render(request, templates)

def get_list_users(request):
    # Получаем отсортированные данные
    users = get_sort_data(request)

    context = {
        'users': users,
    }

    templates = 'users/list_users.html'

    return render(request, templates, context)

def get_list_users_info(request):
    # Получаем отсортированные данные
    users = get_sort_data(request)

    context = {
        'users': users,
    }

    templates = 'users/list_users_info.html'

    return render(request, templates, context)

def get_info_user(request, id):
    user = User.objects.get(id=id)

    context = {
        'user': user,
    }

    templates = 'users/user_info.html'

    return render(request, templates, context)

def sign_user(request):
    context = {}

    templates = 'sign/signup.html'

    return render(request, templates, context)
