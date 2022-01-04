# -*- coding: utf-8 -*-

import datetime

import peewee as pw

db = pw.SqliteDatabase("main.db", pragmas={"foreign_keys": 1})


class HomeworkObjectException(Exception):
    """Not Homework object given"""


class DeadlineException(Exception):
    """Homework deadline expired"""


class BaseModel(pw.Model):
    class Meta:
        database = db  # This model uses the "main.db" database.


class User(BaseModel):
    """Field Types"""

    name = pw.CharField()
    last_name = pw.CharField()


class Teacher(User):
    """
    DB Model for Teachers. Has methods for homework obj manipulation
    """

    """ Field Types """
    id = pw.AutoField(column_name="id", primary_key=True)

    """ Model methods """

    @staticmethod
    def check_homework(homework_result_row):
        if len(homework_result_row.solution) > 5:
            new_hw_done = HomeworkDone(homework_result=homework_result_row)
            new_hw_done.save()

    @staticmethod
    def create_homework(text, deadline):
        created = datetime.datetime.now()
        new_hw = Homework(text=text, created=created, deadline=deadline)
        new_hw.save()

    @staticmethod
    def reset_results():
        HomeworkResult.delete().execute()


class Student(User):
    """
    DB Model for students. Can process homework obj and create hw result
    """

    """ Field Types """
    id = pw.AutoField(column_name="id", primary_key=True)

    """ Model methods """

    def do_homework(self, homework_row, solution):
        """Adds new homework result to results table if deadline isn't expired"""
        if homework_row.is_active():
            new_result = HomeworkResult(author=self, solution=solution, created=homework_row)
            new_result.save()
        else:
            raise DeadlineException("You are late")


class Homework(BaseModel):
    """
    DB Model for homeworks, created by Teachers
    """

    """ Field Types """
    id = pw.AutoField(column_name="id", primary_key=True)

    text = pw.TextField()
    created = pw.DateTimeField()
    deadline = pw.DateTimeField()

    """ Model methods """

    def is_active(self):
        """Checks if homework task is still active and deadline isn't expired'"""

        current_datetime = datetime.datetime.now()
        if current_datetime <= self.deadline:
            return True
        return False


class HomeworkResult(BaseModel):
    """
    DB Model for homework results, created by Students
    """

    """ Field Types """
    id = pw.AutoField(column_name="id", primary_key=True)

    author = pw.ForeignKeyField(Student, backref="student_hw_result", to_field="id", on_delete="CASCADE")  # caution
    solution = pw.TextField()
    created = pw.ForeignKeyField(Homework, backref="hw_results", to_field="id", on_delete="CASCADE")  # caution


class HomeworkDone(BaseModel):
    """Model to store successfully finished homework results after teacher check"""

    """ Field Types """
    id = pw.AutoField(column_name="id", primary_key=True)
    homework_result = pw.ForeignKeyField(HomeworkResult, backref="hw_done", to_field="id", on_delete="CASCADE")


if __name__ == "__main__":

    # db.connect()
    db.create_tables([Teacher, Student, Homework, HomeworkResult, HomeworkDone])

    new_student = Student(name="Boba", last_name="Wachowski")
    new_student2 = Student(name="Biga", last_name="Lebovski")
    new_teacher = Teacher(name="Alex", last_name="Gagarin")

    new_student.save()
    new_student2.save()
    new_teacher.save()

    new_teacher.create_homework(text="Do a trick #1", deadline=datetime.datetime.now() + datetime.timedelta(5))
    new_teacher.create_homework(text="Do a trick #2", deadline=datetime.datetime.now() + datetime.timedelta(5))
    new_teacher.create_homework(text="Do a trick #3", deadline=datetime.datetime.now() + datetime.timedelta(5))
    new_teacher.create_homework(text="Do a trick #4", deadline=datetime.datetime.now() + datetime.timedelta(5))

    # db.close()
    print("DB should be initialised")
