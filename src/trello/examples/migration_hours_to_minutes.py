from django.db import migrations


def convert_estimated_time_from_hours_to_minutes(apps, schema_editor):
    Task = apps.get_model("trello", "Task")  # noqa: N806
    for task in Task.all_objects.all():
        task.estimated_time = task.estimated_time * 60
        task.save()


class Migration(migrations.Migration):

    dependencies = [
        ("trello", "0002_auto_20210622_1217"),
    ]

    operations = [
        migrations.RunPython(
            convert_estimated_time_from_hours_to_minutes, migrations.RunPython.noop
        ),
    ]
