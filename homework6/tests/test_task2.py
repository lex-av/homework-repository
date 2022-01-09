# -*- coding: utf-8 -*-

import datetime

import pytest

from homework6.pack_task2.module_task2 import (
    DeadlineException,
    Homework,
    HomeworkObjectException,
    HomeworkResult,
    Student,
    Teacher,
)


def test_positive_homework_is_active():
    """Checks if deadline calculation is correct on synthetic dates"""

    new_hw = Homework("Homework 1: do sample", 2)
    assert new_hw.is_active()


def test_negative_homework_is_active():
    """Checks if deadline calculation is correct on synthetic dates"""

    new_hw = Homework("Homework 1: do sample", 0)
    new_hw.created = new_hw.created - datetime.timedelta(2)  # Shuffle created parameter 2 days back
    assert not new_hw.is_active()


def test_positive_teacher_homework_creation():
    """Checks that new homework is created and not equal None"""
    teacher = Teacher("Daniil", "Shadrin")
    new_homework = teacher.create_homework("New homework: do it", 2)
    assert new_homework is not None


def test_positive_student_do_active_homework_return_hw_result_obj():
    """Checks that result of doing active homework is HomeworkResult class object"""
    teacher = Teacher("Daniil", "Shadrin")
    new_homework = teacher.create_homework("New homework: do it", 2)
    student = Student("Roman", "Petrov")
    hw_result = student.do_homework(new_homework, "my_precious_solution")

    assert isinstance(hw_result, HomeworkResult)


def test_negative_student_do_expired_homework():
    """Student.do_homework has to raise Exception on doing expired homework"""
    new_hw = Homework("Homework 1: do sample", 0)
    new_hw.created = new_hw.created - datetime.timedelta(2)  # Shuffle created parameter 2 days back
    student = Student("Roman", "Petrov")

    with pytest.raises(DeadlineException):
        student.do_homework(new_hw, "my_precious_solution")


def test_negative_homework_result_gets_non_hw_object():
    """HomeworkResult should not take non homework obj for homework attr"""
    teacher = Teacher("Daniil", "Shadrin")

    with pytest.raises(HomeworkObjectException):
        HomeworkResult("Dude", teacher, "his solution")


def test_positive_homework_done_add_hw():
    """Checks if Teacher.homework_done structure works correctly"""

    opp_teacher = Teacher("Daniil", "Shadrin")
    good_student = Student("Lev", "Sokolov")
    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    opp_teacher.check_homework(result_1)

    # Here we unpack set of results for homework to list and check if first one is HomeworkResult
    assert isinstance(list(Teacher.homework_done[oop_hw])[0], HomeworkResult)


def test_positive_homework_done_remove_hw():
    """
    Checks if Teacher.homework_done structure works
    correctly with all hw deletion
    """

    opp_teacher = Teacher("Daniil", "Shadrin")
    good_student = Student("Lev", "Sokolov")
    oop_hw_1 = opp_teacher.create_homework("Learn OOP", 1)
    result_1 = good_student.do_homework(oop_hw_1, "I have done this hw")
    opp_teacher.check_homework(result_1)
    opp_teacher.reset_results()

    assert not list(Teacher.homework_done[oop_hw_1])


def test_positive_homework_done_remove_specific_hw():
    """
    Checks if Teacher.homework_done structure works
    correctly with specific hw deletion
    """

    opp_teacher = Teacher("Daniil", "Shadrin")
    good_student = Student("Lev", "Sokolov")
    oop_hw_1 = opp_teacher.create_homework("Learn OOP", 1)
    result_1 = good_student.do_homework(oop_hw_1, "I have done this hw")
    opp_teacher.check_homework(result_1)
    opp_teacher.reset_results(oop_hw_1)

    assert not list(Teacher.homework_done[oop_hw_1])
