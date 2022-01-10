# -*- coding: utf-8 -*-

import os

import pytest

from homework8.pack_task2.module_task2 import TableData


def test_positive_len():
    path_to_tests = os.getcwd()
    db_container = TableData(path_to_tests + "/homework8/tests/tst_data/example.sqlite", "books")
    assert len(db_container) == 3


def test_positive_getitem():
    path_to_tests = os.getcwd()
    db_container = TableData(path_to_tests + "/homework8/tests/tst_data/example.sqlite", "books")
    assert db_container["Farenheit 451"] == ("Farenheit 451", "Bradbury")


def test_negative_getitem():
    path_to_tests = os.getcwd()
    db_container = TableData(path_to_tests + "/homework8/tests/tst_data/example.sqlite", "books")
    with pytest.raises(ValueError):
        db_container["Farenheit 45"]


def test_positive_iteration():
    path_to_tests = os.getcwd()
    expected = [("Farenheit 451", "Bradbury"), ("Brave New World", "Huxley"), ("1984", "Orwell")]
    result = []
    db_container = TableData(path_to_tests + "/homework8/tests/tst_data/example.sqlite", "books")
    for book in db_container:
        result.append(book)

    assert result == expected


def test_positive_contains():
    path_to_tests = os.getcwd()
    db_container = TableData(path_to_tests + "/homework8/tests/tst_data/example.sqlite", "books")
    assert "Farenheit 451" in db_container
