# -*- coding: utf-8 -*-

from ..pack_task2.module_task2 import Order, elder_discount, morning_discount


def test_morning_discount():
    ord_1 = Order(100, morning_discount)
    assert ord_1.final_price() == 75.0


def test_elder_discount():
    ord_2 = Order(100, elder_discount)
    assert ord_2.final_price() == 50.0
