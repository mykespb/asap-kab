#! /usr/bin/env python3
# Mikhail Kolodin, 2020
# proc43a.py 2020-11-17 2020-11-19 1.2

# АСАП, КААП
# обработка бард-афиши, DBMS sqlite3, архивист: М.Колодин

import sqlite3
import uuid

dbin  = 'ap.db'
dbout = 'apx.db'

connin  = sqlite3.connect(dbin)
connout = sqlite3.connect(dbout)

ci = connin.cursor()
co = connout.cursor()

sql = '''create table data (
    id integer primary key autoincrement unique not null,
    wd text, year text, date text, datesql text, time text,
    city text, place text, what text, desc text, source text,
    status text, shown text, uuid text
    )'''
co.execute(sql)

rep = 0

for row in ci.execute('select * from data order by datesql asc, time asc'):
    rep += 1
    # ~ if rep > 9: break
    arow = list(row)
    # ~ arow[0] = int(arow[0])
    year = arow[3][:4]
    arow[2:2] = [year]
    arow.append('ok')
    arow.append('shown')
    ui = uuid.uuid4().hex
    arow.append(ui)
    co.execute('insert into data values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', arow)
    connout.commit()

connin.close()
connout.close()

print(f"records written: {rep}")
