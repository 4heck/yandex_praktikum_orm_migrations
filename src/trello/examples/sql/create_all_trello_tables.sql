CREATE TABLE IF NOT EXISTS "trello_project"
(
    "id"            integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "created_at"    datetime     NOT NULL,
    "modified_at"   datetime     NOT NULL,
    "title"         varchar(255) NOT NULL,
    "created_by_id" integer      NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS "trello_column"
(
    "id"            integer          NOT NULL PRIMARY KEY AUTOINCREMENT,
    "created_at"    datetime         NOT NULL,
    "modified_at"   datetime         NOT NULL,
    "title"         varchar(256)     NOT NULL,
    "position"      integer unsigned NOT NULL CHECK ("position" >= 0),
    "created_by_id" integer          NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "project_id"    integer          NOT NULL REFERENCES "trello_project" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS "trello_task"
(
    "id"             integer          NOT NULL PRIMARY KEY AUTOINCREMENT,
    "created_at"     datetime         NOT NULL,
    "modified_at"    datetime         NOT NULL,
    "title"          varchar(255)     NOT NULL,
    "description"    text             NULL,
    "position"       integer unsigned NOT NULL CHECK ("position" >= 0),
    "estimated_time" real             NULL,
    "is_archived"    bool             NOT NULL,
    "column_id"      integer          NOT NULL REFERENCES "trello_column" ("id") DEFERRABLE INITIALLY DEFERRED,
    "created_by_id"  integer          NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS "trello_taskchangelog"
(
    "id"            integer     NOT NULL PRIMARY KEY AUTOINCREMENT,
    "created_at"    datetime    NOT NULL,
    "field"         varchar(55) NOT NULL,
    "old_value"     text        NOT NULL,
    "new_value"     text        NOT NULL,
    "created_by_id" integer     NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "task_id"       integer     NOT NULL REFERENCES "trello_task" ("id") DEFERRABLE INITIALLY DEFERRED
);
