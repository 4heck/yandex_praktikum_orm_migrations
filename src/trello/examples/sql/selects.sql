-- Project.objects.all()
SELECT "trello_project"."id",
       "trello_project"."created_at",
       "trello_project"."created_by_id",
       "trello_project"."modified_at",
       "trello_project"."title"
FROM "trello_project"

-- Task.objects.all()
SELECT "trello_task"."id",
       "trello_task"."created_at",
       "trello_task"."created_by_id",
       "trello_task"."modified_at",
       "trello_task"."title",
       "trello_task"."description",
       "trello_task"."position",
       "trello_task"."column_id",
       "trello_task"."estimated_time",
       "trello_task"."is_archived"
FROM "trello_task"
WHERE "trello_task"."is_archived" = False
ORDER BY "trello_task"."position" ASC

-- TaskChangelog.objects.all()
SELECT "trello_taskchangelog"."id",
       "trello_taskchangelog"."created_at",
       "trello_taskchangelog"."created_by_id",
       "trello_taskchangelog"."task_id",
       "trello_taskchangelog"."field",
       "trello_taskchangelog"."old_value",
       "trello_taskchangelog"."new_value"
FROM "trello_taskchangelog"

-- TaskChangelog.objects.all().select_related("task")
SELECT "trello_taskchangelog"."id",
       "trello_taskchangelog"."created_at",
       "trello_taskchangelog"."created_by_id",
       "trello_taskchangelog"."task_id",
       "trello_taskchangelog"."field",
       "trello_taskchangelog"."old_value",
       "trello_taskchangelog"."new_value",
       "trello_task"."id",
       "trello_task"."created_at",
       "trello_task"."created_by_id",
       "trello_task"."modified_at",
       "trello_task"."title",
       "trello_task"."description",
       "trello_task"."position",
       "trello_task"."column_id",
       "trello_task"."estimated_time",
       "trello_task"."is_archived"
FROM "trello_taskchangelog"
         INNER JOIN "trello_task" ON ("trello_taskchangelog"."task_id" = "trello_task"."id")