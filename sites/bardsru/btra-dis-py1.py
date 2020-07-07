#!/usr/bin/env python3
# brta-s1.py
# Mikhail (myke) Kolodin, 2020
# обработка Bards.ru text archive
# этап 1 - получение списка персон
# этап 1а - разбор полученного списка персон в таб-файл и для экселя
# 2020-07-07 0.1

import re
import sqlite3
import csv

dbname = './brta.db'
csvout = './brta-s1.tsv'

# connect to db
conn = sqlite3.connect(dbname)
db = conn.cursor()

with open(csvout, 'w') as tsv:
    writer = csv.writer (tsv, delimiter='\t')
    writer.writerow (['number', 'fio', 'date_birth', 'date_death', 'page'])
    for row in db.execute ("SELECT pid, fio, dbirth, ddeath, page FROM personsd"):
       writer.writerow (row)

conn.close()
