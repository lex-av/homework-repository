# -*- coding: utf-8 -*-

from unittest import mock

from ..pack_task1.module_task1 import cache


def example_func():
    return 3


@mock.patch("homework3.tests.test_task1.example_func")
def test_cache(mock_example_func):
    decorated_mock_example_func = cache(times=3)(mock_example_func)
    decorated_mock_example_func()
    decorated_mock_example_func()
    decorated_mock_example_func()
    decorated_mock_example_func()

    mock_example_func.assert_called_once()
