# -*- coding: utf-8 -*-

import datetime

from homework5.pack_task1.module_task1 import Homework, Student, Teacher


def test_pos_homework_is_active():
    """Checks if deadline calculation is correct on synthetic dates"""

    new_hw = Homework("Homework 1: do sample", 2)
    assert new_hw.is_active()


def test_pos_homework_is_active_false_output(freezer):
    """Checks if deadline calculation is correct on synthetic dates"""

    new_hw = Homework("Homework 1: do sample", 2)
    current_date = datetime.date.today()
    expired_date = current_date + datetime.timedelta(3)
    freezer.move_to(expired_date.strftime("%d-%m-%Y"))
    assert not new_hw.is_active()


def test_positive_teacher_homework_creation():
    """Checks that new homework is created and not equal None"""
    teacher = Teacher("Daniil", "Shadrin")
    new_homework = teacher.create_homework("New homework: do it", 2)
    assert new_homework is not None


def test_positive_student_do_active_homework():
    """Checks that result of doing active homework isn't none"""
    teacher = Teacher("Daniil", "Shadrin")
    new_homework = teacher.create_homework("New homework: do it", 2)
    student = Student("Roman", "Petrov")
    hw_result = student.do_homework(new_homework)

    assert hw_result is not None


def test_student_do_non_active_homework(freezer):
    """Checks that result of doing non-active homework is none"""
    teacher = Teacher("Daniil", "Shadrin")
    new_homework = teacher.create_homework("New homework: do it", 2)

    current_date = datetime.date.today()
    expired_date = current_date + datetime.timedelta(3)
    freezer.move_to(expired_date.strftime("%d-%m-%Y"))

    student = Student("Roman", "Petrov")
    hw_result = student.do_homework(new_homework)

    assert hw_result is None
