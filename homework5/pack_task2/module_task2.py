"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools
from inspect import signature


def parameters_capture(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__original_func = func

    return wrapper


def deep_wraps(func):
    def inner_wraps(deco_wrapper):
        def wrapper(*args, **kwargs):
            # could assign original func attrs to its initial deco
            # but it seems no need for that

            # deco_wrapper.__name__ = func.__name__
            # deco_wrapper.__doc__ = func.__doc__
            # deco_wrapper.__original_func = func
            # deco_wrapper.__signature__ = signature(func)

            # Assign needed attrs to wrapper of deep_wraps, because it's
            # attrs will be called eventually
            wrapper.__name__ = func.__name__
            wrapper.__doc__ = func.__doc__
            wrapper.__original_func = func
            wrapper.__signature__ = signature(func)

            return func(*args, **kwargs)

        return wrapper

    return inner_wraps


def print_result(func):

    # Place for new decorator
    @deep_wraps(func)  # Takes original func and its decorator
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)

    without_print = custom_sum.__original_func

    print("Down from here should be done")
    # the result returns without printing
    without_print(1, 2, 3, 4)
    print("done")
