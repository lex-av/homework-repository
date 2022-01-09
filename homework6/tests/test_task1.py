# -*- coding: utf-8 -*-

import pytest

from ..pack_task1.module_task1 import User


@pytest.fixture
def create_one_class_instance():
    user_0 = User("Smith")
    yield user_0
    User.reset_instances_counter()


@pytest.fixture
def create_multiple_class_instances():
    _, _, user_b = User("Smith"), User("Smith"), User("Smith")
    yield user_b
    User.reset_instances_counter()


@pytest.fixture
def create_multiple_class_instances_for_reset_return():
    _, _, user_b = User("Smith"), User("Smith"), User("Smith")
    yield user_b
    User.reset_instances_counter()


@pytest.fixture
def create_multiple_class_instances_for_reset_result():
    _, _, user_b = User("Smith"), User("Smith"), User("Smith")
    yield user_b
    User.reset_instances_counter()


def test_positive_instances_counter_no_instances():
    assert User.get_created_instances() == 0


def test_positive_instances_counter_just_one_instance(create_one_class_instance):
    assert create_one_class_instance.get_created_instances() == 1


def test_positive_instances_counter_multiple_instances(create_multiple_class_instances):
    assert create_multiple_class_instances.get_created_instances() == 3


def test_positive_instances_counter_reset_return(create_multiple_class_instances_for_reset_return):
    assert create_multiple_class_instances_for_reset_return.reset_instances_counter() == 3


def test_positive_instances_counter_reset_result(create_multiple_class_instances_for_reset_result):
    create_multiple_class_instances_for_reset_result.reset_instances_counter()
    assert create_multiple_class_instances_for_reset_result.get_created_instances() == 0


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
