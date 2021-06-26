# У нас уже есть 1 Task c таким текстом:
# Я потрачу на эту задачу больше часов, чем планировал!
# Мы хотим создать побольше копий его и потом во всех сразу
# заменить слово "часов" на "минут" ¯\_(ツ)_/¯

from django.contrib.auth import get_user_model

from trello.models import Task

User = get_user_model()

user = User.objects.all().first()

base_text = "Я потрачу на эту задачу больше часов, чем планировал!"

task = Task.objects.create(created_by=user, title=base_text)

# создаем
for _ in range(1, 10):
    task.pk = None
    task.save()

# обновляем по очереди
for task in Task.objects.all():
    task.text = task.text.replace("часов", "минут")
    task.save()

# происходит магия ✨🧸🦋🧿🌈☁️ и мы понимаем, что все успеем

# обновляем все вместе
Task.objects.all().update(title="Я все успею вовремя!")
