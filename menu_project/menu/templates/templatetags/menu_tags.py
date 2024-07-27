from django import template
from menu_project.menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_items': []}

    request = context['request']
    current_path = request.path

    menu_items = menu.items.all()
    active_item = None

    # Определяем активный элемент
    for item in menu_items:
        if current_path.startswith(item.get_url()):
            active_item = item
            break

    # Функция для построения дерева меню
    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, parent=item)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': item == active_item or any(child['is_active'] for child in children)
                })
        return tree

    menu_tree = build_tree(menu_items)

    return {'menu_tree': menu_tree}
