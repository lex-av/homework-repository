# -*- coding: utf-8 -*-
"""
Task definition format is too complex for comment
Gotta leave a link here:
https://github.com/lex-av/epam_python_autumn_2020/blob/main/lecture_08_object_model/hw/task2.rst
"""

import sqlite3


class TableData:
    """Data container for database files"""

    db_tables = tuple()
    db_tables_rows = dict()

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name


def scrub(table_name):
    return "".join(char for char in table_name if char.isalnum())


def prototype_method_len_using_count(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) from " + scrub(table_name))
    table_len = cursor.fetchone()
    conn.close()

    return table_len


def prototype_method_get_tables(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = [items[0] for items in cursor.fetchall()]
    conn.close()

    return table_names


def prototype_method_get_table_columns(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * from " + scrub(table_name))
    columns_names = list(map(lambda x: x[0], cursor.description))
    conn.close()

    return columns_names


# def prototype_method_update_table(database_name, table_name):
#     ...


if __name__ == "__main__":
    books_table_len = prototype_method_len_using_count("example.sqlite", "books")
    db_tables = prototype_method_get_tables("example.sqlite")
    db_table_columns = prototype_method_get_table_columns("example.sqlite", "books")

    print()
