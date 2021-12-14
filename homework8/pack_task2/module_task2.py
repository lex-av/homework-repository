# -*- coding: utf-8 -*-
"""
Task definition format is too complex for comment
Gotta leave a link here:
https://github.com/lex-av/epam_python_autumn_2020/blob/main/lecture_08_object_model/hw/task2.rst
"""

import sqlite3


class TableData:
    """Data container for database files"""

    def _get_table_columns(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * from " + self._scrub(self.table_name))
        columns = [description[0] for description in cursor.description]
        conn.close()

        return columns

    @staticmethod
    def _scrub(table_name):
        """Service method to erase any possible injections from query"""
        return "".join(char for char in table_name if char.isalnum())

    def _current_table_len(self):
        """Service method to update len of iterating table"""

        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) from " + self._scrub(self.table_name))
        table_len = cursor.fetchone()[0]
        conn.close()

        return table_len

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.current_row = 0
        self.last_row = 0

    def __getitem__(self, item):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        search_column = self._get_table_columns()[0]
        table_name = self._scrub(self.table_name)

        cursor.execute("SELECT " + self._get_table_columns()[0] + " from " + self._scrub(self.table_name))
        search_result = [result[0] for result in cursor.fetchall()]

        if item in search_result:
            cursor.execute("SELECT * from " + table_name + " WHERE " + search_column + " = " + "'" + str(item) + "'")
            line = cursor.fetchall()
            return line[0]
        else:
            raise ValueError

    def __next__(self):
        self.last_row = self._current_table_len()

        if self.current_row < self.last_row:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * from " + self._scrub(self.table_name) + " LIMIT 1 OFFSET " + str(self.current_row))
            table_row = cursor.fetchall()[0]
            conn.close()
            self.current_row += 1

            return table_row
        else:
            self.current_row = 0
            raise StopIteration

    def __iter__(self):
        return self

    def __len__(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) from " + self._scrub(self.table_name))
        table_len = cursor.fetchone()
        conn.close()

        return table_len


if __name__ == "__main__":
    db_container = TableData("example.sqlite", "books")
    db_container_iterator = iter(db_container)
    for row in db_container:
        print(row)

    for row in db_container:
        print(row)

    print(db_container["Farenheit 451"])
    print()
