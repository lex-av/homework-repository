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
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
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


class Student:
    """Class for student definition"""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    """Class for teacher definition"""

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, deadline):
        return Homework(text, deadline)


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
    """Class for homework results definition"""

    def __init__(self, author, homework, solution):
        self.homework = homework  # Add exception-logic here
        self.solution = solution
        self.author = author
        self.created = homework.created


if __name__ == "__main__":
    ...
