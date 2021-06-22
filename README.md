# ORM and migrations demo webinar code | Yandex Praktikum 

## Install required dependencies
```shell
pip install -r requirements.txt
```

## Тезисы вебинара

### Смотрим на первую версию моделей
- choices
- [Meta options](https://docs.djangoproject.com/en/3.2/ref/models/options/)
- [кастомные менеджеры моделей](https://docs.djangoproject.com/en/3.2/topics/db/managers)
- как устроено сохранение changelog

### Замечаем несоблюдение DRY
- миксины для моделей
- [абстрактные модели](https://docs.djangoproject.com/en/3.2/topics/db/models/#abstract-base-classes)
  
### Смотрим на количество миграций, замечаем что их можно схлопнуть
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

### Замечаем, что в поле estimated_time храним время в часах и пишем миграцию на хранение в минутах
- [кастомные миграции](https://docs.djangoproject.com/en/3.2/howto/writing-migrations/)
- [копирование объектов модели](https://docs.djangoproject.com/en/3.2/topics/db/queries/#copying-model-instances)
- [обновление объектов](https://docs.djangoproject.com/en/3.2/topics/db/queries/#copying-model-instances) - update_queryset.py

### Замечаем, что в файле trello/models.py у нас слишком много всего
- разделение моделей по модулям, как работает

### Прочее
- [F](https://docs.djangoproject.com/en/3.2/ref/models/expressions/#django.db.models.F)
- [Q](https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects)
- [model methods](https://docs.djangoproject.com/en/3.2/topics/db/models/#model-methods)
- get_absolute_url() 
- переопределение метода save()
- метод init
- through