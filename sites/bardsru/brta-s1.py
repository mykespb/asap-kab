#!/usr/bin/env python3
# brta-s1.py
# Mikhail (myke) Kolodin, 2020
# обработка Bards.ru text archive
# этап 1 - получение списка авторов
# 2020-07-07 1.1

import re
import requests
from lxml import html
import sqlite3
import time

print ("Работа с текстовым архивом сайта www.bards.ru - 1 этап: получение списка авторов")

site_addr = 'http://www.bards.ru/'
start_addr = 'http://bards.ru/archives/index.php'
author_addr = 'http://bards.ru/archives/'
dbname = './brta.db'
print (site_addr, start_addr, author_addr, dbname)

#sub_letters = "C0,C1,C2,C3,C4,C5,A8,C6,C7,C8,C9,CA,CB,CC,CD,CE,CF,D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,Dd,De,DF".split(",")
#sub_letters = "CC,CD,CE,CF,D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,DD,DE,DF".split(",")
sub_letters = ['C0']
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

def run_letter (leta):
    """ run with specific letter"""

    print ("запуск для кода", leta)
    gaddr = start_addr + '?ch=%' + leta
    page = requests.get (gaddr)
    page.encoding = 'cp1251'
    parsed = html.fromstring (page.text)

    try:
        authors = parsed.xpath('//a[starts-with(@href,"author.php")]')
        for a in authors:
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

                apage = author_addr + ref[0]
                ypage = apage + "&sortyear=1"

#                print (0, end=',')

                ppage = requests.get (apage)
                ppage.encoding = 'cp1251'
                pparsed = html.fromstring (ppage.text)

                bio = pparsed.xpath('//tr/td[@class="show"]')[0].xpath('string(.)')

#                print (1, end=',')

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

#                print (2, end=',')

                try:
                    address = pparsed.xpath('//tr/td[@class="address"]')[0].xpath('string(.)')
                except:
                    print ("no address")
                    address = ''

                print ("### result:", (numba, refaut, name, desc[0], yearbirth, yeardeath))

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
conn.close()

# -----------------------------
