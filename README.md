# ORM and migrations demo webinar code | Yandex Praktikum 

## Install required dependencies
```shell
pip install -r requirements.txt
```

## Краткий экскурс в проект — что мы хотим спроектировать (models_v1)
- обзор Trello
- обзор моделей

## Что такое миграции?
- миграции django по умолчанию
- фиксированная директория
- команды для создания и применения (+ указание приложения, указание имени миграции)
- таблица django_migrations для хранения примененных миграций

## Рефакторинг — замечаем несоблюдение DRY (models_v2)
- миксины для моделей
- [абстрактные модели](https://docs.djangoproject.com/en/3.2/topics/db/models/#abstract-base-classes)

## Требование от заказчика — архивные задачи должны показываться только в админке и больше нигде (models_v3)
- что такое менеджер модели?
- [кастомные менеджеры моделей](https://docs.djangoproject.com/en/3.2/topics/db/managers)
- переопределение методов админки

## Рефакторинг — разделяем модели по модулям (models_v4)

## Требование от заказчика — сохранять историю действий с задачей (models_v5)
- переопределение метода save() - как устроено сохранение changelog

## Требование от заказчика — хранить время в часах неудобно, нужно перевести на минуты
- [кастомные миграции](https://docs.djangoproject.com/en/3.2/howto/writing-migrations/)
- [копирование объектов модели](https://docs.djangoproject.com/en/3.2/topics/db/queries/#copying-model-instances)
- [обновление объектов](https://docs.djangoproject.com/en/3.2/topics/db/queries/#copying-model-instances) - update_queryset.py

## Рефакторинг — сжимаем миграции
- ручное сжатие миграций
```shell
python manage.py migrate trello zero
rm trello/migrations/*
touch trello/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
```
- [squashmigrations](https://docs.djangoproject.com/en/3.2/topics/migrations/#migration-squashing)
```shell
python manage.py squashmigrations trello <migration_name>
```

### Прочее
- [Q](https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects)
- [model methods](https://docs.djangoproject.com/en/3.2/topics/db/models/#model-methods)
- get_absolute_url() 
- through