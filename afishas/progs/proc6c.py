#! /usr/bin/env python3
# Mikhail Kolodin, 2020
# proc6b.py 2020-11-19 2020-11-19 0.1

# АСАП, КААП
# обработка бард-афиши, дамп DBMS sqlite3 в tab- файл, архивист: М.Колодин

import sqlite3

db  = 'apx.db'
txt = 'apx.tab'

conn = sqlite3.connect(db)
cur  = conn.cursor()

rep = 0

with open(txt, 'w') as tf:

    tf.write("id wd  year    date    datesql time    city    place   what    desc    source  status  shown   uuid\n")

    for row in cur.execute('select * from data order by datesql asc, time asc'):
        rep += 1
        print(rep % 10, end="", flush=True)
        # ~ if rep > 9: break
        a = list(row)

        a[7] = a[7].strip()
        a[8] = a[8].strip()
        a[9] = a[9].strip()
        a[10] = a[10].strip()
        a[11] = a[11].strip()
        a[12] = a[12].strip()

        #0  1    2       3    4    5     6    7    8      9      10    11   12 13
        #N  wd year date datesql time city place what desc source status shown uuid\n')

        tf.write(f"{a[0]}\t{a[1]}\t{a[2]}\t{a[3]}\t{a[4]}\t{a[5]}\t{a[6]}\t{a[7]}\t{a[8]}\t{a[9]}\t{a[10]}\t{a[11]}\t{a[12]}\t{a[13]}\n")

conn.close()

print(f"обработано событий: {rep}")
