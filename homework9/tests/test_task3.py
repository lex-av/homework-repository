# -*- coding: utf-8 -*-

from pathlib import Path

from ..pack_task3.module_task3 import universal_file_counter


def test_positive_no_tokens():
    tests_data_path = Path.cwd() / "homework9/tests/tests_data/test_task3"

    assert universal_file_counter(tests_data_path, "txt") == 3


def test_positive_w_tokens():
    tests_data_path = Path.cwd() / "homework9/tests/tests_data/test_task3"

    assert universal_file_counter(tests_data_path, "txt", str.split) == 4
