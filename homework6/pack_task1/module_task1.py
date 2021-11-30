# -*- coding: utf-8 -*-
"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""
    cls.instances_number = 0

    def instances_number_increase():
        """Internal service func"""
        cls.instances_number += 1

    def __init__(self=cls):
        """Init for increasing count on object creation"""
        # Я на самом деле не понял, почему сработало именно так
        # Сначала пытался использовать self.instances_number += 1 или cls.instances_number += 1

        # self=cls выглядит как костыль, чтобы вызывать методы из инстансов и от класса, но может так и надо
        instances_number_increase()

    def reset_instances_counter(self=cls):
        """Object attribute"""
        saved_number = self.instances_number
        self.instances_number = 0
        return saved_number

    def get_created_instances(self=cls):
        """Object attribute"""
        return self.instances_number

    setattr(cls, __init__.__name__, eval(__init__.__name__))
    setattr(cls, reset_instances_counter.__name__, eval(reset_instances_counter.__name__))
    setattr(cls, get_created_instances.__name__, eval(get_created_instances.__name__))

    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":
    print("Expected 0: ", User.get_created_instances())
    user, user_a, user_b = User(), User(), User()
    print("Expected 3: ", user.get_created_instances())
    print("Expected 3: ", user.reset_instances_counter())
    print("Expected 0: ", user.get_created_instances())
    print()
