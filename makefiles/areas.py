# -- coding: utf-8 --
import sqlite3
from sys import argv

script, db_file = argv
areas = [
    [
        'Halden',
        'Fredrikstad',
        'Sarpsborg',
        'Mysen',
        'Moss'
    ],
    [
        'Drøbak',
        'Asker og Bærum',
        'Romerike',
        'Jessheim'
    ],
    [
        'Oslo'
    ],
    [
        'Hamar',
        'Elverum',
        'Tynset',
        'Kongsvinger'
    ],
    [
        'Lillehammer',
        'Otta',
        'Gjøvik',
        'Fagernes'
    ],
    [
        'Ringerike',
        'Hallingdal',
        'Drammen',
        'Kongsberg'
    ],
    [
        'Horten',
        'Tønsberg',
        'Larvik',
        'Sandefjord'
    ],
    [
        'Skien',
        'Notodden',
        'Rjukan'
    ],
    [
        'Arendal',
        'Setesdal'
    ],
    [
        'Kristiansand',
        'Mandal',
        'Flekkefjord'
    ],
    [
        'Stavanger',
        'Egersund',
        'Haugesund'
    ],
    [
        'Bergen',
        'Voss',
        'Stord',
        'Odda'
    ],
    [
        'Førde',
        'Nordfjordeid',
        'Sogndal'
    ],
    [
        'Ålesund',
        'Ørsta',
        'Molde',
        'Kristiansund',
        'Sunndalsøra'
    ],
    [
        'Trondheim',
        'Støren',
        'Orkdal',
        'Brekstad'
    ],
    [
        'Steinkjer',
        'Levanger',
        'Stjørdal',
        'Namsos'
    ],
    [
        'Mosjøen',
        'Mo i Rana',
        'Bodø',
        'Fauske',
        'Narvik',
        'Svolvær',
        'Sortland'
    ],
    [
        'Storslett',
        'Harstad',
        'Tromsø',
        'Svalbard',
        'Finnsnes'
    ],
    [
        'Vadsø',
        'Kirkenes',
        'Alta',
        'Hammerfest',
        'Lakselv'
    ]
]

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

for i in range(len(areas)):
    for area in areas[i]:
        input = "INSERT INTO area VALUES(null,'%s',%d)" % (area, i + 1)
        cursor.execute(input)

connection.commit()
connection.close()
