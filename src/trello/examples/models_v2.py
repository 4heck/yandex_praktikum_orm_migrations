from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class ModifiedAtMixin(models.Model):
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModelMixin(CreatedAtMixin, CreatedByMixin, ModifiedAtMixin):
    class Meta:
        abstract = True


class Project(BaseModelMixin):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Column(BaseModelMixin):
    title = models.CharField(max_length=256)
    position = models.PositiveIntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.project})"

    class Meta:
        ordering = ["position"]


class Task(BaseModelMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    estimated_time = models.FloatField(help_text="in hours", blank=True, null=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

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
