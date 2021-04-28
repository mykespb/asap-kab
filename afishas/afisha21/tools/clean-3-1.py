#!/usr/bin/env python3

# чистка БД с афишей -архивом АП
# вер. 2021-04-24 0.1

import sqlite3
import json
from pprint import pprint as pp
from uuid import uuid4 as uu

dbfile  = './ap-in.db'

conn = sqlite3.connect(dbfile)
cursor = conn.cursor()

def ch1():
    cursor.execute("""alter table data add column dtsql text """)
    conn.commit()

def ch2():
    cursor.execute("""update data set
        dtsql = datesql || " " || time,
        year = substr(datesql, 1, 4)
        """)
    conn.commit()

def sub3(col, sfrom, sto):
    """ замена строк в полях таблицы"""
    print(f"меняем {col=}: {sfrom=} -> {sto=}")
    sql = '''update data set
        %s = "%s"
        where %s = "%s" ''' % (col, sto, col, sfrom)
    print(sql)
    cursor.execute(sql)
    conn.commit()

def ch3():
    """набор правок в полях"""
    sub3('city', "г.Гатчина", "Гатчина")
    sub3('city', "г,Гатчина", "Гатчина")
    sub3('city', "СПь", "СПб")
    sub3('city', "Спб", "СПб")
    sub3('city', "г.Пушкин", "Пушкин")
    sub3('city', "г.Ломоносов", "Ломоносов")
    sub3('city', "д.Федоровское", "Федоровское")
    sub3('city', "д. Федоровское", "Федоровское")
    sub3('city', "г.Всеволожск", "Всеволожск")
    sub3('city', "д.Низино", "Низино")
    sub3('city', "дер.", "деревня")
    sub3('city', "пос.Новоселки", "Новосёлки")
    sub3('city', "пос.Кузьмолово", "Кузьмолово")
    sub3('city', "пос. Кузьмолово", "Кузьмолово")
    sub3('city', "Кяндикюля", "Кандикюля")
    sub3('city', "дер. Коккорево, берег Ладожского озера", "Коккорево")

def ch4():
    """удалить лишнее"""
    cursor.execute('''delete from data
        where city = 'city'
        ''')
    conn.commit()

def ch5():
    """учесть отмены"""
    print("учёт отмен")
    sql = """update data set
        status = 'cancel'
        where desc like '%отмена%' or desc like '%ОТМЕНА%' """
    cursor.execute(sql)
    conn.commit()

def ch6():
    """почистить строки"""
    print("чистка строк")
    sql = """update data set
        desc = replace(desc, '""', '"') """
    cursor.execute(sql)
    sql = """update data set
        desc = replace(desc, '''''', '''') """
    cursor.execute(sql)
    sql = """update data set
        what = replace(what, '""', '"') """
    cursor.execute(sql)
    sql = """update data set
        what = replace(what, '''''', '''') """
    cursor.execute(sql)
    conn.commit()

# ~ ch1()
# ~ ch2()
# ~ ch3()
# ~ ch4()
# ~ ch5()
ch6()

conn.close()
