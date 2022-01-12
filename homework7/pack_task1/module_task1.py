"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""

import collections.abc
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
        "not_simple_key:": [["RED"], ["RED"], [["RED"]]],  # Modded a new key here for tests
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


def find_occurrences(obj: dict, element: Any) -> int:
    """Recursive search through nested structure. No loop detection"""

    if obj == element:
        return 1

    if isinstance(obj, str):
        if obj == element:
            return 1
        else:
            return 0

    if isinstance(obj, collections.abc.Mapping):
        return sum(find_occurrences(dct_sub_obj, element) for dct_sub_obj in obj.values())

    if isinstance(obj, collections.abc.Sequence):
        return sum(find_occurrences(lst_sub_obj, element) for lst_sub_obj in obj)


if __name__ == "__main__":
    pass
