# -*- coding: utf-8 -*-

import sqlite3


def scrub(table_name):
    """Function to erase any possible injections from query"""
    return "".join(char for char in table_name if char.isalnum())


def prototype_method_len_using_count(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) from " + scrub(table_name))
    table_len = cursor.fetchone()
    conn.close()

    return table_len


def prototype_method_get_all(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * from " + scrub(table_name))
    table_len = cursor.fetchall()
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


def prototype_method_get_one_line(database_name, table_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * from " + scrub(table_name) + " WHERE name = " + "'Farenheit 451'")
    columns_names = cursor.fetchall()
    conn.close()

    return columns_names


if __name__ == "__main__":
    books_table_len = prototype_method_len_using_count("example.sqlite", "books")
    books_table = prototype_method_get_all("example.sqlite", "books")
    db_tables = prototype_method_get_tables("example.sqlite")
    db_table_columns = prototype_method_get_table_columns("example.sqlite", "books")
    res = prototype_method_get_one_line("example.sqlite", "books")
