# -*- coding: utf-8 -*-
"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimpleEnum(type):  # is a metaclass
    def __new__(mcs, name, bases, dct):
        simple_enum_cls = super().__new__(mcs, name, bases, dct)

        # Attrs stored in private __keys, so:
        if any([not key.startswith("_") for key in dct.keys()]):
            raise AttributeError()

        enum_attrs = []
        for attr, value in dct.items():
            if attr.endswith("__keys"):
                enum_attrs = value

        simple_enum_cls._member_names_ = []
        for attr in enum_attrs:
            setattr(simple_enum_cls, attr, attr)
            simple_enum_cls._member_names_.append(attr)

        return simple_enum_cls

    def __getitem__(cls, key):
        return getattr(cls, key.upper())

    def __iter__(cls):
        return (name for name in cls._member_names_)

    def __len__(cls):
        return len(cls._member_names_)


class ColorsEnum(metaclass=SimpleEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimpleEnum):
    __keys = ("XL", "L", "M", "S", "XS")


if __name__ == "__main__":
    print()
    pass
