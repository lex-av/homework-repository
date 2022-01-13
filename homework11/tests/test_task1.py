# -*- coding: utf-8 -*-

import pytest

from ..pack_task1.module_task1 import SimpleEnum


def test_pos_get_item():
    class ColorsEnum(metaclass=SimpleEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum["RED"] == "RED"


def test_pos_dot_item():
    class ColorsEnum(metaclass=SimpleEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"


def test_pos_len():
    class ColorsEnum(metaclass=SimpleEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert len(ColorsEnum) == 4


def test_neg_attr_error():
    with pytest.raises(AttributeError):

        class ColorsEnum(metaclass=SimpleEnum):
            keys = ("RED", "BLUE", "ORANGE", "BLACK")

        len(ColorsEnum)
