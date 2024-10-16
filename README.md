# Skystore

Skystore — это интернет-магазин, предназначенный для хранения и продажи плагинов и примеров кода.

## Структура проекта

- **config/**: Корневая директория проекта Django.
- **catalog/**: Приложение, в котором хранятся все модели, вьюшки и шаблоны для отображения каталога.
- **templates/**: Директория с HTML-шаблонами для рендеринга страниц.
- **static/**: Статические файлы, такие как CSS и JavaScript.

## Установка и запуск

Следуй этим шагам для установки и запуска проекта:

1. Настройка виртуального окружения:   
- python -m venv venv
- venv\Scripts\activate
- pip install django 
- pip install django psycopg2-binary
- python manage.py runserver
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

2. Откройте в браузере
- Перейдите на http://127.0.0.1:8000 для просмотра проекта.
3. Настройте базу данных PostgreSQL
4. Настройте базу данных PostgreSQL:
```bash
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql_psycopg2',
             'NAME': 'yourdatabase',
             'USER': 'yourusername',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
