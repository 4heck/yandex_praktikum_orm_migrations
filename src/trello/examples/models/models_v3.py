from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s" + "s")

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
    title = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="columns")

    def __str__(self):
        return f"{self.title} ({self.project})"

    class Meta:
        ordering = ["position"]


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=False)


class ArchivedTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived=True)


class AllTaskManager(models.Manager):
    use_in_migrations = True


class Task(BaseModelMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="tasks")
    estimated_time = models.FloatField(help_text="in hours", blank=True, null=True)
    is_archived = models.BooleanField(default=False)

    objects = TaskManager()
    archived_objects = ArchivedTaskManager()
    all_objects = AllTaskManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["position"]
