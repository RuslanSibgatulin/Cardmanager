# Cardman - менеджер бонусных карт.
![CI Result](https://github.com/RuslanSibgatulin/Cardmanager/actions/workflows/test.yml/badge.svg)

Веб-приложение для управления базой данных бонусных карт (карт лояльности, кредитных карт и т.д).


## Используемые технологии
- Код приложения на Python
- Фреймворк [Django 4.1](https://docs.djangoproject.com/en/4.1/)
- Очередь задач [Celery](https://docs.celeryq.dev/en/stable/#) + Redis
- СУБД - Postgres
- Все компоненты системы запускаются через Docker-compose.

# Запуск приложения
## Клонировать репозиторий
    git@github.com:RuslanSibgatulin/Cardmanager.git

## Переменные окружения
Подготовить файлы с переменными окружения по аналогии с файлами `docker/envs/*.example` и пересохранить в файлы `*.env`.
Обязательно указать значение переменной `DJANGO_SECRET_KEY`.

## Запуск

    make start

### При первичном запуске необходимо выполнить команды инициализации
    make init
    make static

# Функциональность
- [Главная страница приложения](http://127.0.0.1/cards/)
- [Админ-панель](http://127.0.0.1/admin/)
