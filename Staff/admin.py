from django.contrib.admin import ModelAdmin
from django.contrib.admin import site, register
from .models import Position, User


class PositionAdmin(ModelAdmin):
    # Отображение списка должностей
    list_display = ('name', 'id')
site.register(Position, PositionAdmin)


@register(User)
class UserAdmin(ModelAdmin):
    # Отображение списка сотрудников
    list_display = ('name', 'id', 'fk_position', 'date',)
    # Отображение фильтра по должности
    list_filter = ('fk_position', 'date',)
    # Структура при добавлении данных о сотруднике
    fieldsets = (
                  ('Список должностей', {
                      'fields': (
                          'fk_position',
                      )
                  }),
                  ('Информация о сотруднике', {
                      'fields': (
                          'name',
                          'date',
                          'amount',
                          'photo',
                      )
                  }),
    )
