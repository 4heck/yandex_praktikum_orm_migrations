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
