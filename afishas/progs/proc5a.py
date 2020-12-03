#! /usr/bin/env python3
# Mikhail Kolodin, 2020
# proc43a.py 2020-11-17 2020-11-19 1.2

# АСАП, КААП
# обработка бард-афиши, объединение таблиц (таб) и DBMS sqlite3, архивист: М.Колодин

import os
import pathlib
import sqlite3
import uuid

db  = 'apx.db'

conn = sqlite3.connect(db)
cur  = conn.cursor()

filesproc = 0
rep = 0
errs = 0

cwd = pathlib.Path('.')
patn = "*.tab"

for tab in cwd.glob(patn):
    print(f"\n-----------------------------\nработаем с базой {tab}", flush=True)

    with open(tab) as inf:

        for ln, line in enumerate(inf):

            if ln == 0: continue
            print(ln % 10, end="", flush=True)

            data = line.split('\t')

            while len(data) < 11:
                data.append("")

            y = data[2][:4]
            data[1:1] = [y]

            ui = uuid.uuid4().hex
            data.append(ui)

            try:
                cur.execute('insert into data values(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
                conn.commit()
                rep += 1
            except:
                errs += 1

conn.close()

print(f"\n-------------------------\nдобавлено событий: {rep}, ошибок: {errs}", flush=True)
