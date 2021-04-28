#!/usr/bin/env python3

# объединение 2 баз sqlte3 в формате json в один файл db
# вер. 2021-04-24 1.2

import sqlite3
import json
from pprint import pprint as pp
from uuid import uuid4 as uu

tin1 = './apx.json'
tin2 = './ap.json'

tout = './apz1.json'

conn = sqlite3.connect("apz1.db")
cursor = conn.cursor()

cursor.execute("""create table data
(id integer primary key autoincrement unique not null,
wd, year, date, datesql, time, city, place, what, desc, source,
status, shown, uuid
)
""")

with open(tin1) as fin:
    data = json.load(fin)

print(f"база 1. получили событий: {len(data)}")

for n, ev in enumerate(data):
    # ~ pp(ev)
    # ~ if n >= 5: break
    if n % 100 == 0:
        print(n, end=", ")

    cols = ", ".join(ev.keys())
    quests1 = '?' * len(ev.keys())
    quests = ','.join(quests1)
    vals = [str(x) for x in ev.values()]
    sql = f"insert into data ({cols}) values({quests})"
    cursor.execute(sql, vals)

conn.commit()

with open(tin2) as fin:
    data = json.load(fin)

print(f"\n\nбаза 2. получили событий: {len(data)}")

same = other = 0

for n, ev in enumerate(data):
    vals = [ev['date'], ev['time'], ev['place'], ev['what']]
    if n <= 5:
        pp(ev)
        pp(vals)
        # ~ break
    if n % 100 == 0:
        print(n, end=", ")

    check = """select count(*) from data
        where date = {}
        and time = {}
        and place = {}
        and what = {}""".format(
            ev['date'], ev['time'], ev['place'], ev['what'])

    cursor.execute("""select count(*) from data
        where date = ?
        and time = ?
        and place = ?
        and what = ?""", vals)
    cur_result = cursor.fetchone()
    sameq = int(cur_result[0])

    if sameq == 0:
        other += 1
        uc = uu().hex
        del ev['id']
        ev['status'] = 'ok'
        ev['shown'] = 'shown'
        ev['desc'] = ev['desc'].replace('\r', '')
        cols = ", ".join(ev.keys())  + ", uuid"
        quests1 = '?' * (len(ev.keys()) +1)
        quests = ','.join(quests1)
        vals = [str(x) for x in ev.values()]
        vals += [uc]
        sql = f"insert into data ({cols}) values({quests})"
        print("\nother:", other, vals)
        cursor.execute(sql, vals)

    else:
        same += 1

conn.commit()

print(f"\n{same=}, {other=}")

conn.close()
