from django.contrib import admin

from trello.models import Column, Project, Task


class TaskAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = self.model.all_objects.get_queryset()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs  # noqa: R504

    list_display = ("__str__", "is_archived")


admin.site.register(Project)
admin.site.register(Column)
admin.site.register(Task, TaskAdmin)
