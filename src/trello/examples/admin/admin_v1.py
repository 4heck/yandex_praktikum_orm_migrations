from django.contrib import admin

from trello.models import Column, Project, Task

admin.site.register(Project)
admin.site.register(Column)
admin.site.register(Task)
