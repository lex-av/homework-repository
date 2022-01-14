# -*- coding: utf-8 -*-

"""
We have a file that works as key-value storage, each line is represented as key and value separated by = symbol,
example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string,
it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and values accessible as collection
items and as attributes.

Example: storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence. In case when value cannot be assigned to an
attribute (for example when there's a line 1=something) ValueError should be raised. File size is expected
to be small, you are permitted to read it entirely into memory.
"""


class KeyValueStorage:
    """Tool for converting text files into dict-like structure"""

    key_value_storage = {}

    class Decorators:
        """Storage for file_synchronizer for its proper work"""

        @classmethod
        def _file_synchronizer(cls, method):
            """Rewrites file to sync with key-value storage"""

            def wrapper(self, *args):
                result = method(self, *args)
                with open(self.filepath, "w") as src:
                    for key, value in self.key_value_storage.items():
                        src.write(f"{key}={value}\n")

                return result

            return wrapper

    def __init__(self, filepath):
        self.filepath = filepath
        self.keys_values_raw = []

        with open(filepath) as source:
            for line in source:
                key, value = line.strip().split("=")
                try:
                    hash(key)
                    try:
                        self.key_value_storage[key] = int(value)
                        setattr(self, key, int(value))

                    except ValueError:
                        self.key_value_storage[key] = value
                        setattr(self, key, value)
                except TypeError:
                    raise ValueError("Wrong key")

    @Decorators._file_synchronizer
    def __setitem__(self, key, value):
        self.key_value_storage[key] = value

    def __getitem__(self, key):
        if key in self.key_value_storage:
            return self.key_value_storage[key]
        else:
            raise KeyError("Key doesn't exist")

    @Decorators._file_synchronizer
    def __delitem__(self, key):
        if key in self.key_value_storage:
            del self.key_value_storage[key]
        else:
            raise Exception("Software Name doesn't exist")

    def __len__(self):
        return len(self.key_value_storage)


if __name__ == "__main__":
    pass
