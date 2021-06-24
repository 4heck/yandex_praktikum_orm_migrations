CREATE TABLE IF NOT EXISTS "trello_project"
(
    "id"            integer      NOT NULL PRIMARY KEY AUTOINCREMENT,
    "created_at"    datetime     NOT NULL,
    "modified_at"   datetime     NOT NULL,
    "title"         varchar(255) NOT NULL,
    "created_by_id" integer      NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);