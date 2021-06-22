from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import models

from trello.models.column import Column
from trello.models.mixins import BaseModelMixin, CreatedAtMixin, CreatedByMixin

User = get_user_model()


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False)


class ArchivedTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=True)


class Task(BaseModelMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    estimated_time = models.FloatField(help_text="in minutes", blank=True, null=True)
    is_archived = models.BooleanField(default=False)

    objects = TaskManager()
    archived_objects = ArchivedTaskManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        for field, _ in TaskChangelogType:
            setattr(self, f"old_{field}", getattr(self, field))

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
        self.handle_changelog()

    def handle_changelog(self):
        created_by = get_current_user()

        if created_by:
            for field, _ in TaskChangelogType:

                new_value = getattr(self, field)
                old_value = getattr(self, f"old_{field}")

                if new_value and new_value != old_value:
                    TaskChangelog.objects.create(
                        task=self,
                        field=field,
                        old_value=old_value,
                        new_value=new_value,
                        created_by=created_by,
                    )

    class Meta:
        ordering = ["position"]


class TaskComment(BaseModelMixin):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} ({self.task})"


TaskChangelogType = [
    ("title", "title"),
    ("description", "description"),
    ("column", "column"),
    ("estimated_time", "estimated_time"),
]


class TaskChangelog(CreatedAtMixin, CreatedByMixin, models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    field = models.CharField(max_length=55, choices=TaskChangelogType)
    old_value = models.TextField()
    new_value = models.TextField()

    def __str__(self):
        return f"{self.task} ({self.field}: {self.old_value} -> {self.new_value})"
