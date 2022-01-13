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


def instance_counter_inheritance(cls):
    """
    This deco uses inheritance strategy:
    - Create new class, inherited from
    - Add functionality to new class
    - return new inherited class

    This strat leads to some rules in next possible
    inheritance:
    New inherited class should contain following func:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    to call counting or other parent-inits
    """

    class ModifiedOrig(cls):
        """New inherited class supporting instance counting"""

        def __init__(self, *args, **kwargs):
            """
            1) Init instances counter
            2) Increment it by 1, because instance is being created
            3) Call original __init__
            """

            self.init_counter_on_instance_creation()
            super().__init__(*args, **kwargs)

        @classmethod
        def init_counter_on_instance_creation(cls):
            """
            This counting initializer increments instance
            counter when instance is created
            (also creates counter attribute if it's not present
            in class namespace)
            """

            if "instances_counter" not in cls.__dict__:
                cls.instances_counter = 1
            else:
                cls.instances_counter += 1

        @classmethod
        def init_counter(cls):
            """
            This counting initializer is used in situations,
            when instance is not being created, so it only
            initialise counter is it's not present in class
            namespace.
            """
            if "instances_counter" not in cls.__dict__:
                cls.instances_counter = 0

        @classmethod
        def get_created_instances(cls):
            cls.init_counter()
            return cls.instances_counter

        @classmethod
        def reset_instances_counter(cls):
            cls.init_counter()
            try:
                return cls.instances_counter
            finally:
                cls.instances_counter = 0

    return ModifiedOrig


@instance_counter_inheritance
class User:
    name = "Dave"

    def __init__(self, last_name):
        self.last_name = last_name


if __name__ == "__main__":
    pass
