# -*- coding: utf-8 -*-

import peewee as pw
import playhouse.migrate as pm

from homework12.pack_task1.db_models import (
    Homework,
    HomeworkDone,
    HomeworkResult,
    Student,
    Teacher,
)


def initialise_db_structure():
    """Tool to create new db structure"""
    db = pw.SqliteDatabase("main.db")
    db.create_tables([Teacher, Student, Homework, HomeworkResult, HomeworkDone])
    return db


def initialise_migrator():
    """Tool to initialise migrator for existing db"""
    db = pm.SqliteDatabase("main.db")
    migrator = pm.SqliteMigrator(db)
    return migrator


# Не понимаю, как бы я тут мог использовать функционал миграций
# при задаче просто инициализировать структуру

# title_field = pm.CharField(default="")
# status_field = pm.IntegerField(null=True)
#
# pm.migrate(
#     migrator.add_column("some_table", "title", title_field),
#     migrator.add_column("some_table", "status", status_field),
#     migrator.drop_column("some_table", "old_column"), )


if __name__ == "__main__":
    initialise_db_structure()
