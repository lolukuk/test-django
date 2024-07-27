from django import template
from menu.models import Menu, MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu, parent=None)
        return {'menu_items': menu_items}
    except ObjectDoesNotExist:
        return {'menu_items': []}
