from django import template
from menu.models import Menu, MenuItem  # Исправление импорта

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    # Логика для получения меню по имени
    request = context['request']
    menu = Menu.objects.get(name=menu_name)
    menu_items = MenuItem.objects.filter(menu=menu)
    return {
        'menu': menu,
        'menu_items': menu_items,
        'current_path': request.path,
    }
