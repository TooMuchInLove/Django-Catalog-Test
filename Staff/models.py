from django.db.models import Model, ForeignKey
from django.db.models import CharField, TextField
from django.db.models import IntegerField
from django.db.models import DateField
from django.db.models import ImageField
from django.db.models import SET_NULL

from django.utils import timezone


class Position(Model):
    # Должность сотрудника
    name = CharField(null=True, max_length=100, verbose_name='Должность сотрудника')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self): # __str__ применяется для отображения объекта в интерфейсе
        return self.name


class User(Model):
    # Вторичный ключ должности (обязательно)
    fk_position = ForeignKey(Position, null=True, on_delete=SET_NULL, verbose_name='Должность сотрудника')
    # ФИО сотрудника
    name = CharField(null=True, max_length=100, verbose_name='ФИО сотрудника')
    # Дата приема на работу
    date = DateField(default=timezone.now().strftime('%d.%m.%Y'), verbose_name='Дата приёма на работу')
    # Размер заработной платы
    amount = IntegerField(default=0, null=True, blank=True, verbose_name='Размер заработной платы')
    # Фото сотрудника
    photo = ImageField(upload_to='images/users', height_field=None, width_field=None,
                       max_length=100, blank=True, verbose_name='Фото сотрудника')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    # __str__ применяется для отображения объекта в интерфейсе
    def __str__(self):
        return self.name
