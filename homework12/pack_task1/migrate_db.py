# -*- coding: utf-8 -*-

import playhouse.migrate as pm

my_db = pm.SqliteDatabase("main.db")
migrator = pm.SqliteMigrator(my_db)

title_field = pm.CharField(default="")
status_field = pm.IntegerField(null=True)

pm.migrate(
    migrator.add_column("some_table", "title", title_field),
    migrator.add_column("some_table", "status", status_field),
    migrator.drop_column("some_table", "old_column"),
)
