# -*- coding: utf-8 -*-

import pytest

from homework7.pack_task1.module_task1 import find_occurrences_v1

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

single_elemets = [({"a": 45}, 45, 1), ({"a": False}, False, 1), ({"a": "abcd"}, "abcd", 1)]

strings_with_multiple_elem_to_search = [
    ({"b": "redredred"}, "red", 3),
    ({"b": "redred"}, "red", 2),
    ({"b": "red2rediiiiiiired"}, "red", 3),
]


nested_cases = [
    ({"b": {"b": {"b": "redredred"}}}, "red", 3),
    ({"b": [[[False]]]}, False, 1),
    ({"b": {"c": [[[45]]]}}, 45, 1),
]


def test_positive_on_example_tree():
    assert find_occurrences_v1(example_tree, "RED") == 6


@pytest.mark.parametrize("tree, elem_to_search, output", single_elemets)
def test_positive_single_elements(tree, elem_to_search, output):
    assert find_occurrences_v1(tree, elem_to_search) == output


@pytest.mark.parametrize("tree, elem_to_search, output", strings_with_multiple_elem_to_search)
def test_positive_strings_with_multiple_elem_to_search(tree, elem_to_search, output):
    assert find_occurrences_v1(tree, elem_to_search) == output


@pytest.mark.parametrize("tree, elem_to_search, output", nested_cases)
def test_positive_nested_cases(tree, elem_to_search, output):
    assert find_occurrences_v1(tree, elem_to_search) == output
