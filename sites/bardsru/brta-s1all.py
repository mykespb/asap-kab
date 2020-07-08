#!/usr/bin/env python3
# brta-s1all.py
# Mikhail (myke) Kolodin, 2020
# обработка Bards.ru text archive
# этап 1 - получение списка авторов
# 2020-07-06 2020-07-08 1.3.2

import re
import requests
from lxml import html
import sqlite3
import time

print ("Работа с текстовым архивом сайта www.bards.ru - 1 этап: получение списка авторов по полному списку персон")

useDB = 1

site_addr = 'http://www.bards.ru/'
start_addr = 'http://bards.ru/persons.php?ch=%'
author_addr = 'http://bards.ru/person.php?id='
dbname = './brtall.db'
print (site_addr, start_addr, author_addr, dbname)

sub_letters = "C0,C1,C2,C3,C4,C5,A8,C6,C7,C8,C9,CA,CB,CC,CD,CE,CF,D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,DA,DD,DE,DF".split(",")
#sub_letters = ['C0']
print (sub_letters)

# connect to db
conn = sqlite3.connect(dbname)
db = conn.cursor()

# -----------------------------

def run_sub():
    """ run with all sub_letters"""

    print ("запуск для всех букв")
    for sub in sub_letters:
        run_letter(sub)

# -----------------------------

def run_person (numba, name, desc):
    """ run for specific person"""

    numba = str(numba)
    print ("запуск для кода", numba)

    apage = author_addr + numba
    refaut = apage
    ppage = requests.get (apage)
    ppage.encoding = 'cp1251'
    pparsed = html.fromstring (ppage.text)

    bio = pparsed.xpath('//tr/td[@class="show"]')[0].xpath('string(.)')

    print (1, end=',')

    yearbirth = re.search (r'род. ([\d.]+)', bio)
    if yearbirth:
        yearbirth = yearbirth[0].split()[1]
    else:
        yearbirth = '-'
    yeardeath = re.search (r'ум. ([\d.]+)', bio)
    if yeardeath:
        yeardeath = yeardeath[0].split()[1]
    else:
        yeardeath = '-'

    print (2, yearbirth, yeardeath)

    try:
        address = pparsed.xpath('//tr/td[@class="address"]')[0].xpath('string(.)')
    except:
        print ("no address")
        address = ''

    print ("### result:", (numba, refaut, name, desc[0], yearbirth, yeardeath))

    if useDB:
        print ("writing to DB", end=" --> ")
        print ("data:", (str(numba), str(refaut), str(name), str(address), str(bio), str(yearbirth), str(yeardeath), str(desc[0])))
        try:
            db.execute("INSERT INTO personsd (pid, page, fio, desc, bio, dbirth, ddeath, place) VALUES (?,?,?,?,?,?,?,?)", (str(numba), str(refaut), str(name), str(address), str(bio), str(yearbirth), str(yeardeath), str(desc[0])))
            conn.commit()
            print ("ok!")
        except:
            print ("cannot write to DB!")

# -----------------------------

def run_letter (leta):
    """ run with specific letter"""

    print ("запуск для кода", leta)
    gaddr = start_addr + leta
    page = requests.get (gaddr)
    page.encoding = 'cp1251'
    parsed = html.fromstring (page.text)
#    print (8)

    try:
        authors = parsed.xpath('//a[starts-with(@href,"person.php")]')
#        print(authors)
        for a in authors:
#            print(9)
            try:
                time.sleep(3)
                ref  = a.xpath('@href')
                name = a.xpath('text()')[0]
                numba = re.search (r'(\d+)$', ref[0])[0]

                print ("*** person:", name, numba)

#                if name <= 'Мирошниченко':
#                    print ("!!! пропущено !!!")
#                    continue

                desc = a.xpath('../following-sibling::*/text()')
                refaut = author_addr + ref[0]

#                apage = author_addr + ref[0]
                apage = author_addr + numba
                ypage = apage + "&sortyear=1"

                print (0, refaut, numba, apage)

                ppage = requests.get (apage)
                ppage.encoding = 'cp1251'
                pparsed = html.fromstring (ppage.text)

                bio = pparsed.xpath('//tr/td[@class="show"]')[0].xpath('string(.)')

                print (1, end=',')

                yearbirth = re.search (r'род. ([\d.]+)', bio)
                if yearbirth:
                    yearbirth = yearbirth[0].split()[1]
                else:
                    yearbirth = '-'
                yeardeath = re.search (r'ум. ([\d.]+)', bio)
                if yeardeath:
                    yeardeath = yeardeath[0].split()[1]
                else:
                    yeardeath = '-'

                print (2, yearbirth, yeardeath)

                try:
                    address = pparsed.xpath('//tr/td[@class="address"]')[0].xpath('string(.)')
                except:
                    print ("no address")
                    address = ''

                print ("### result:", (numba, refaut, name, desc[0], yearbirth, yeardeath))

                if useDB:
                    print ("writing to DB", end=" --> ")
                    print ("data:", (str(numba), str(refaut), str(name), str(address), str(bio), str(yearbirth), str(yeardeath), str(desc[0])))
                    try:
                        db.execute("INSERT INTO personsd (pid, page, fio, desc, bio, dbirth, ddeath, place) VALUES (?,?,?,?,?,?,?,?)", (str(numba), str(refaut), str(name), str(address), str(bio), str(yearbirth), str(yeardeath), str(desc[0])))
                        conn.commit()
                        print ("ok!")
                    except:
                        print ("cannot write to DB!")

            except:
                print ("exception inner")

    except:
        print ("exception outer")

# -----------------------------

def main():
    """ main routine"""
    run_sub()

# -----------------------------

main()

#run_person(8105, "Пятницкая Татьяна Анатольевна", "[Россия, Иркутская область, Иркутск] (род. 11.10.1971)")

conn.close()

# -----------------------------
