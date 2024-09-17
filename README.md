# Getting started
![PyPI - Version](https://img.shields.io/pypi/v/django?style=for-the-badge&logo=django&logoColor=green&label=Django&labelColor=%23092E20&color=%2383B81A&cacheSeconds=https%3A%2F%2Fpypi.org%2Fproject%2FDjango%2F)

---

### Установка проекта

1. Клонируем проект:
```bash
git clone https://github.com/SilverSheldon/Brendwall_test_task.git
```
2. Подтягиваем зависимости:
```bash
pip install -r requirements.txt
```

---

### Запуск проекта
1. Не забудьте применить миграции:
```bash
python manage.py migrate
```
2. Запуск на отладочном веб-сервере:
```bash
python manage.py runserver
```

---

### Возможности проекта
1. Эндпоинт на фронте:

    http://localhost:8000/api/v1.0/add_product/

2. При желании погонять через Postman (или Browsable API от DRF) можно использовать следующий эндпоинт:

    http://localhost:8000/api/v1.0/products/

    Собственно, сюда же и делаются fetch-запросы.