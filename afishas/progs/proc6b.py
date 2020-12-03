#! /usr/bin/env python3
# Mikhail Kolodin, 2020
# proc6a.py 2020-11-18 2020-11-19 1.1

# АСАП, КААП
# обработка бард-афиши, обработка базы DBMS sqlite3, архивист: М.Колодин

import sqlite3

db  = 'apx.db'

conn = sqlite3.connect(db)
curr  = conn.cursor()
curw  = conn.cursor()

rep = 0
err = 0

for row in curr.execute('select * from data order by datesql asc, time asc'):
#    if rep > 1: break
    rep += 1
    print(rep % 10, end="", flush=True)

    a = list(row)

    id = a[0]
    # ~ print(id, end=", ")
    # ~ print(len(a))

    for i in range(1, len(a)):
        a[i] = a[i].strip()
        a[i] = a[i].replace('\n', ' ')
        a[i] = a[i].replace('\r', ' ')
        a[i] = a[i].replace('\t', ' ')

    sql = """update data set
        wd = ?,
        year = ?,
        date = ?,
        datesql = ?,
        time = ?,
        city = ?,
        place = ?,
        what = ?,
        desc = ?,
        source = ?,
        status = ?,
        shown = ?,
        uuid = ?
        where id = ?
        """

    dats = a[1:] + [a[0]]

    # ~ print(sql, dats, "len:", len(dats))

    curw.execute(sql, dats)
    conn.commit()

conn.close()

print(f"\nобработано событий: {rep}, ошибок: {err}\n")
