# Productlab тестовое задание Python
<img src="https://img.shields.io/badge/python-3.10-green"></img>
<img src="https://img.shields.io/badge/django-3.26-green"></img>
### Установка необходимым зависимостей

```sh
pip install -r requirements.txt
```

### Указать настройки PostgreSQL базы

```sh
export DB_NAME=""
export DB_USER=""
export DB_PASSWORD=""
export DB_HOST=""
export DB_PORT=5432
```

### Миграция данных

```sh
python manage.py migrate
```

### Запуск Django сервера

```sh
python manage.py runserver
```

### Для удобства тестирования

Мною была добавление документация с помощью <a href="https://github.com/axnsan12/drf-yasg">drf-yasg</a>.

Доступно как <a href="http://127.0.0.1:8000/swagger"><b>Swagger</b></a>, так и <a href="http://127.0.0.1:8000/redoc"><b>Redoc</b></a> документация.
