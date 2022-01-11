# -*- coding: utf-8 -*-
"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineException с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""


import datetime
from collections import defaultdict
from random import choices


class HomeworkObjectException(Exception):
    """Not Homework object given"""


class DeadlineException(Exception):
    """Homework deadline expired"""


class Person:
    """Basic parameters: FirstName and Lastname"""

    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    """Class for student definition"""

    @staticmethod
    def chance_of_success(probability: float) -> bool:
        """
        Returns true with given probability/chance.
        probability = 0.8 means 80% for True and 20% for False
        """

        return choices((True, False), (probability, 1 - probability))[0]

    def do_homework(self, homework, student_solution):
        if homework.is_active():
            return HomeworkResult(self, homework, student_solution)
        raise DeadlineException("You are late")


class Teacher(Person):
    """Class for teacher definition"""

    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @staticmethod
    def check_homework(hw_result):
        if len(hw_result.solution) > 5:
            Teacher.homework_done[hw_result.homework].add(hw_result)
            return True
        return False

    @staticmethod
    def reset_results(homework=None):
        if homework is None:
            Teacher.homework_done = defaultdict(set)
        else:
            Teacher.homework_done.pop(homework)


class Homework:
    """Class for homework definition and deadline check"""

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self):
        """Checks if homework task is still active and deadline isn't expired'"""

        current_datetime = datetime.datetime.now()
        if current_datetime <= self.created + datetime.timedelta(self.deadline):
            return True
        return False


class HomeworkResult:
    """
    Class for homework results definition.
    Has to be returned by do_homework method in Student
    """

    def __init__(self, author, homework, solution):
        self.author = author
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise HomeworkObjectException("You gave a not Homework object")
        self.solution = solution
        self.created = homework.created


if __name__ == "__main__":
    new_teacher = Teacher("Albus", "Dumbledor")
    print()

    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")

    # try:
    #     result_4 = HomeworkResult(good_student, "fff", "Solution")
    # except Exception:
    #     print('There was an exception here')
    opp_teacher.check_homework(result_1)
    # temp_1 = opp_teacher.homework_done
    #
    # advanced_python_teacher.check_homework(result_1)
    # temp_2 = Teacher.homework_done
    # assert temp_1 == temp_2
    #
    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    # Teacher.reset_results()
