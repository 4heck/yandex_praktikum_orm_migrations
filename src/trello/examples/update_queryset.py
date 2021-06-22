# У нас уже есть 1 TaskComment c таким текстом:
# Я потрачу на эту задачу больше часов, чем планировал!
# Мы хотим создать побольше копий его и потом во всех сразу
# заменить слово "часов" на "минут" ¯\_(ツ)_/¯

from trello.models import Task, TaskComment, User

user = User.objects.all().first()
task = Task.objects.all().first()

base_text = "Я потрачу на эту задачу больше часов, чем планировал!"

task_comment = TaskComment.objects.create(created_by=user, task=task, text=base_text)

# создаем
for _ in range(1, 10):
    task_comment.pk = None
    task_comment.save()

# обновляем по очереди
for task_comment in TaskComment.objects.all():
    task_comment.text = task_comment.text.replace("часов", "минут")
    task_comment.save()

# происходит магия ✨🧸🦋🧿🌈☁️ и мы понимаем, что все успеем

# обновляем все вместе
TaskComment.objects.all().update(text="Я все успею вовремя!")
