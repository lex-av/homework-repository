# -*- coding: utf-8 -*-
# Create your models here.

import datetime

from django.db import models
from django.utils import timezone


class HomeworkObjectException(Exception):
    """Not Homework object given"""


class DeadlineException(Exception):
    """Homework deadline expired"""


class User(models.Model):
    """Field Types"""

    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    class Meta:
        abstract = True


class Teacher(User):
    """
    DB Model for Teachers. Has methods for homework obj manipulation
    """

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
        HomeworkDone.objects.all().delete()


class Student(User):
    """
    DB Model for students. Can process homework obj and create hw result
    """

    """ Model methods """

    def do_homework(self, homework_row, solution):
        """Adds new homework result to results table if deadline isn't expired"""
        if homework_row.is_active():
            HomeworkResult.objects.create(author=self, solution=solution, created=homework_row)
        else:
            raise DeadlineException("You are late")


class Homework(models.Model):
    """
    DB Model for homeworks, created by Teachers
    """

    """ Field Types """

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    """ Model methods """

    def is_active(self):
        """Checks if homework task is still active and deadline isn't expired'"""

        current_datetime = timezone.now()
        if current_datetime <= self.deadline:
            return True
        return False


class HomeworkResult(models.Model):
    """
    DB Model for homework results, created by Students
    """

    """ Field Types """

    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.ForeignKey(Homework, on_delete=models.CASCADE)


class HomeworkDone(models.Model):
    """Model to store successfully finished homework results after teacher check"""

    """ Field Types """
    homework_result = models.ForeignKey(HomeworkResult, on_delete=models.CASCADE)
