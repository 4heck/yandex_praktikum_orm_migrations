from django.db import models

from trello.models.mixins import BaseModelMixin


class Project(BaseModelMixin):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
