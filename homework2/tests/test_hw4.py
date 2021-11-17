# -*- coding: utf-8 -*-
from ..pack_hw4.module_hw4 import *


def test_hw4_decorator():
    cache_func = cache(functional)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
