# -*- coding: utf-8 -*-
"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount_method programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""

from typing import Callable


class Order:
    def __init__(self, price: int, discount_method: Callable):
        self.price = price
        self.discount_method = discount_method

    def final_price(self):
        return self.discount_method(self)


def morning_discount(order_obj):
    return order_obj.price * 0.75


def elder_discount(order_obj):
    return order_obj.price * 0.5


if __name__ == "__main__":
    ord_1 = Order(100, morning_discount)
    print(ord_1.final_price())

    ord_2 = Order(100, elder_discount)
    print(ord_2.final_price())
