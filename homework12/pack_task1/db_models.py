# -*- coding: utf-8 -*-

import datetime as dt

import peewee as pw

db = pw.SqliteDatabase(
    "main.db",
)


class BaseModel(pw.Model):
    class Meta:
        database = db  # This model uses the "main.db" database.


class User(BaseModel):
    name = pw.CharField()
    last_name = pw.CharField()


class Teacher(User):
    teacher_id = pw.AutoField(column_name="TeacherId", primary_key=True)


class Student(User):
    student_id = pw.AutoField(column_name="StudentId", primary_key=True)


class Homework(BaseModel):
    homework_id = pw.AutoField(column_name="HomeworkId", primary_key=True)

    text = pw.TextField()
    created = pw.DateTimeField()
    deadline = pw.DateTimeField()


class HomeworkResult(BaseModel):
    homework_result_id = pw.AutoField(column_name="HomeworkResultId", primary_key=True)

    author = pw.ForeignKeyField(Teacher, backref="homework_result")  # caution
    solution = pw.TextField()
    created = pw.ForeignKeyField(Homework, backref="homework_result", to_field="created")  # caution


if __name__ == "__main__":

    # db.connect()
    db.create_tables([Teacher, Student, Homework, HomeworkResult])

    new_student = Student(name="Bob", last_name="Wachowski")
    new_student2 = Student(name="Boba", last_name="Wachowski")
    new_teacher = Teacher(name="Alex", last_name="Wachowski")
    new_hw = Homework(text="Do the trick №1", created=dt.datetime.now(), deadline=dt.datetime.now() + dt.timedelta(5))
    new_hw_res = HomeworkResult(author=new_teacher, solution="I done trick №1", created=new_hw)

    new_student.save()
    new_student2.save()
    new_teacher.save()
    new_hw.save()
    new_hw_res.save()
    db.close()
    print("DB should be initialised")
