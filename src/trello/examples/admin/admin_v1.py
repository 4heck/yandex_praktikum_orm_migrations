from django.contrib import admin

from trello.models import Column, Project, Task, TaskComment

admin.site.register(Project)
admin.site.register(Column)
admin.site.register(Task)
admin.site.register(TaskComment)
