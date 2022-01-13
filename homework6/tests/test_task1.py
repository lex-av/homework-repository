# -*- coding: utf-8 -*-

from ..pack_task1.module_task1 import User


def test_positive_instances_counter_no_instances():
    assert User.get_created_instances() == 0


def test_positive_instances_counter_just_one_instance():
    user_0 = User("Smith")
    count = user_0.get_created_instances()
    User.reset_instances_counter()
    assert count == 1


def test_positive_instances_counter_multiple_instances():
    _, _, user_b = User("Smith"), User("Smith"), User("Smith")
    count = user_b.get_created_instances()
    User.reset_instances_counter()
    assert count == 3


def test_positive_instances_counter_reset_return():
    _, _, user_b = User("Smith"), User("Smith"), User("Smith")
    assert user_b.reset_instances_counter() == 3


def test_positive_instances_counter_reset_result():
    _, _, user_b = User("Smith"), User("Smith"), User("Smith")
    user_b.reset_instances_counter()
    count = user_b.reset_instances_counter()
    assert count == 0


def test_pos_instances_counter_with_deeper_inheritance():
    class Teacher(User):
        """Some test class"""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    assert Teacher.get_created_instances() == 0


def test_pos_instances_counter_with_deeper_inheritance_new_instance_creation():
    class Teacher(User):
        """Some test class"""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    new_teacher = Teacher("Smith")
    assert new_teacher.get_created_instances() == 1
