#! /usr/bin/env python3
# Mikhail Kolodin, 2020
# proc6a.py 2020-11-18 2020-11-19 1.2

# АСАП, КААП
# обработка бард-афиши, дамп DBMS sqlite3 в текстовый файл для простого приятного чтения, архивист: М.Колодин

import sqlite3

db  = 'apx.db'
txt = 'apx.txt'

conn = sqlite3.connect(db)
cur  = conn.cursor()

rep = 0

with open(txt, 'w') as tf:

    for row in cur.execute('select * from data order by datesql asc, time asc'):
        rep += 1
        print(rep % 10, end="", flush=True)
        # ~ if rep > 9: break
        a = list(row)

        if a[1] == 'wd':
            continue

        a[7] = a[7].strip()
        a[8] = a[8].strip()
        a[9] = a[9].strip()
        a[10] = a[10].strip()
        a[11] = a[11].strip()
        a[12] = a[12].strip()

        #0  1    2  3    4       5     6    7    8      9      10    11   12   13
        #N  wd year date datesql time city place what desc source status shown uuid\n')

        print(a[1], a[2], a[3], a[4], a[5], a[6], a[7], file=tf)
        if a[8]:
            print(a[8], file=tf)
        if a[9]:
            print(a[9], file=tf)
        if a[10]:
            print(a[10], file=tf)
        print(a[11], a[12], a[13], '\n', file=tf)

conn.close()

print(f"обработано событий: {rep}")
