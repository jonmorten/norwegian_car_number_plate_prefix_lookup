# coding: utf-8


import json
import sqlite3


class Db(object):
    """
    SQLite DB wrapper
    """

    connection = None
    cursor = None

    def _dict_factory(self, cursor, row):
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
        return d

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.connection.row_factory = self._dict_factory
        self.cursor = self.connection.cursor()

    def __del__(self):
        if not self.connection is None:
            self.connection.close()

    def fetchall(self, sql, to_json=True):
        if self.cursor is None:
            return ''
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if to_json is True:
            return json.dumps(result)
        else:
            return result
