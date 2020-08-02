#!/usr/bin/python3

# kab/asap project
# mkff-moder1.py
# Mikhail (myke) Kolodin, 2020
# 2020-08-02 0.1
# fill database mkff from excel file with joint bards archives data

import pymysql
import pymysql.cursors

import datetime as dt

# ------------------------------------------

host = 'localhost'
db   = 'mkff'
user = 'bard'
pasw = 'bard'
cset = 'cp1251'

# ------------------------------------------

print ("Start working...")

#con = pymysql.connect(host=host, user=user, password=pasw, db=db, charset=cset)
con = pymysql.connect(host=host, user=user, password=pasw, db=db, charset=cset, cursorclass=pymysql.cursors.DictCursor)

# ------------------------------------------

print("\n-----------------------------\nSchemes\n")

# sheet1 scheme
ss1 = "number record_code archive_owner digitize device_no file_name no_on_device timer quality song_line1 rem_date_work song_name singer rem_singer song_author music_author rem_music verses_author record_type record_owner archive_code name_coded line1_coded music_coded author_coded verses_coded uuid_record uuid_original etc_auto rem_dt quality_coded dt_exec".split()
ss1nk = {k: v for k, v in enumerate(ss1)}
ss1kn = {v: k for k, v in enumerate(ss1)}
print("ss1nk", ss1nk)
print("ss1kn", ss1kn)

# sheet1 scheme
ss2 = "number fname fext filename fpath ftype fullpath".split()
ss2nk = {k: v for k, v in enumerate(ss2)}
ss2kn = {v: k for k, v in enumerate(ss2)}
print("ss2nk", ss2nk)
print("ss2kn", ss2kn)

# ------------------------------------------

def test1():
    """simply test db connect"""

    global con, cur

    cur.execute("SELECT VERSION() as ver")
    version = cur.fetchone()
    print("Database version: {}".format(version['ver']))

    cur.execute("select * from main limit 1")
    desc = cur.description
#    print ("---\ndesc:", desc)
    pdesc = [a[0] for a in desc]
    print ("---\npretty desc:", pdesc)

#        pretty desc: ['number', 'record_code', 'archive_owner', 'digitize', 'device_no', 'file_name', 'no_on_device', 'timer', 'quality', 'song_line1', 'rem_date_work', 'song_name', 'singer', 'rem_singer', 'song_author', 'music_author', 'rem_music', 'verses_author', 'record_type', 'record_owner', 'archive_code', 'name_coded', 'line1_coded', 'music_coded', 'author_coded', 'verses_coded', 'uuid_record', 'uuid_original', 'etc_auto', 'rem_dt', 'quality_coded', 'dt_exec']

    cur.execute("select * from arch limit 1")
    desc = cur.description
#    print ("---\ndesc:", desc)
    pdesc = [a[0] for a in desc]
    print ("---\npretty desc:", pdesc)

# ------------------------------------------

def main():
    """general starter"""

    global con, cur

    print("\n-----------------------------\nProcessing\n")

    with con:
        with con.cursor() as cur:
        #cur = con.cursor()

            test1()

    print("\n-----------------------------\nStopping\n")

# ------------------------------------------

main()

#con.close()
print ("Work is over.")

# ------------------------------------------

# =ЕСЛИ(ЕНД(ВПР(D6689;$Лист3.$A$3:$I$15790;8;2=5));ЕСЛИ(ЕНД(ВПР(D6689;$Лист3.$B$3:$I$15790;7;2=5));"нет файла";ГИПЕРССЫЛКА(ВПР(D6689;$Лист3.$B$3:$I$15790;7;2=5);"Скачать"));ГИПЕРССЫЛКА(ВПР(D6689;$Лист3.$A$3:$I$15790;8;2=5);"Скачать"))

