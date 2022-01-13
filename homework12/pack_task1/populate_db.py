# -*- coding: utf-8 -*-

import datetime

import peewee as pw

from homework12.pack_task1.db_models import Student, Teacher


def populate_db():
    db = pw.SqliteDatabase("main.db")
    db.connect()

    new_student = Student(name="Bob", last_name="Smith")
    new_student2 = Student(name="Will", last_name="Smith")
    new_teacher = Teacher(name="Alex", last_name="Baker")

    new_student.save()
    new_student2.save()
    new_teacher.save()

    new_teacher.create_homework(text="Do a trick #1", deadline=datetime.datetime.now() + datetime.timedelta(5))
    new_teacher.create_homework(text="Do a trick #2", deadline=datetime.datetime.now() + datetime.timedelta(5))
    new_teacher.create_homework(text="Impossible #1", deadline=datetime.datetime.now() + datetime.timedelta(-5))
    new_teacher.create_homework(text="Impossible #2", deadline=datetime.datetime.now() + datetime.timedelta(0))

    db.close()


if __name__ == "__main__":
    populate_db()
