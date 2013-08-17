# -- coding: utf-8 --
import sqlite3
from sys import argv

script, db_file = argv
counties = [
    'Østfold',
    'Akershus',
    'Oslo',
    'Hedmark',
    'Oppland',
    'Buskerud',
    'Vestfold',
    'Telemark',
    'Aust-Agder',
    'Vest-Agder',
    'Rogaland',
    'Hordaland',
    'Sogn og Fjordane',
    'Møre og Romsdal',
    'Sør-Trøndelag',
    'Nord-Trøndelag',
    'Nordland',
    'Troms',
    'Finnmark'
]

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

for county in counties:
    cursor.execute("INSERT INTO county VALUES (null,'" + county + "')")

connection.commit()
connection.close()
