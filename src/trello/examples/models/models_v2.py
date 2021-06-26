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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["position"]
