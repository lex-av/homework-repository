"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
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


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Recursive search of element through given dict-tree.
    """

    # Accumulator common parameter for search-funcs
    acc = 0

    def search_non_nested(item, item_to_search):
        """
        Function for search and check in str and non iterable objects
        in base case of nested search func
        """
        nonlocal acc

        if type(item) == str == type(item_to_search):
            acc += item.count(item_to_search)

        elif isinstance(item, (bool, int)) and isinstance(item_to_search, (bool, int)):
            if item == item_to_search:
                acc += 1

    def search_nested(structure, element_to_search):
        """
        Recursive function to search through nested structures.
        Uses non iterable objects and especially str to define base case of recursion.
        For base case (single element in any iterable) search_non_nested func used
        """

        structure_to_iterate = None  # If no need to iterate

        if isinstance(structure, str):
            search_non_nested(structure, element_to_search)  # Base case

        else:
            try:
                structure_to_iterate = iter(structure)

            except TypeError:
                search_non_nested(structure, element_to_search)  # Base case

            # Recursion case
            if isinstance(structure, dict):
                structure_to_iterate = structure.values()

            if structure_to_iterate:
                for current_element in structure_to_iterate:
                    search_nested(current_element, element_to_search)

    # Actual search call here
    search_nested(tree, element)

    return acc


if __name__ == "__main__":
    print()
    print(find_occurrences(example_tree, "RED"))  # 6
