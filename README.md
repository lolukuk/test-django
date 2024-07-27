
## Django Menu Project

Этот проект реализует систему меню на Django. В этом проекте реализована структура меню и подменю с использованием моделей Django и шаблонных тегов.

### Содержание

- [Требования](#требования)
- [Установка](#установка)
- [Настройка](#настройка)
- [Создание меню](#создание-меню)
- [Использование](#использование)
- [Примечания](#примечания)

### Требования

- Python 3.9+ (Был использован 3.12)
- Django 4.2+ (Был использован 5.2)

### Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/lolukuk/test-django.git
   cd test-django
   ```

2. **Создайте виртуальное окружение и активируйте его:**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Для Linux: source venv/bin/activate 
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

### Настройка

1. **Проверьте файл настроек `settings.py`:**

   В данном решении была использована SQLite:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

2. **Примените миграции если потребуется:**

   ```bash
   python manage.py migrate
   ```

### Создание меню

1. **Запустите shell или используйте базовый cpython:**

   ```bash
   python manage.py shell
   ```

2. **Создайте меню и элементы меню:**

   Ниже был использован простой пример для создания древовидной структуры:

   ```python
   from menu.models import Menu, MenuItem

   # Создание меню, если оно не существует
   if not Menu.objects.filter(name='main_menu').exists():
       main_menu = Menu.objects.create(name='main_menu')

   # Создание элементов меню
   menu_item1 = MenuItem.objects.create(menu=main_menu, name='Home', url='/')
   menu_item2 = MenuItem.objects.create(menu=main_menu, name='About', url='/about')
   menu_item3 = MenuItem.objects.create(menu=main_menu, name='Contact', url='/contact')

   # Создание подменю
   submenu_item1 = MenuItem.objects.create(menu=main_menu, name='Team', url='/about/team', parent=menu_item2)
   submenu_item2 = MenuItem.objects.create(menu=main_menu, name='History', url='/about/history', parent=menu_item2)
   ```

### Использование

1. **Запустите сервер разработки:**

   ```bash
   python manage.py runserver
   ```

2. **Откройте браузер и перейдите по адресу:**

   ```
   http://127.0.0.1:8000/
   ```

   Вы должны увидеть меню на главной странице.

### Примечания

- Убедитесь, что приложение `menu` добавлено в `INSTALLED_APPS` в `settings.py`.
- Для корректного отображения меню необходимо наличие хотя бы одного элемента меню в базе данных.
