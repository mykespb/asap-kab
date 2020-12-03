#! /usr/bin/env python3
# Mikhail Kolodin, 2020
# proc1a.py 2020-11-17 1.3

# АСАП, КААП
# обработка бард-афиши 1998-2003 годов, архивист: М.Колодин

from datetime import date

infile  = './1998-2003u.tab'
outfile = './out-1998-2003u.tab'

cit1 = "СПб Лосево Гатчина Пушкин Новгород г.Пушкин г.Гатчина Сосновый дер. Выборг".split()
cit2 = "иПб СПи".split()

def tofile (so):
    """ print simple line s"""
    global outf, rem, outs, state

    ls = so.split('\t')
    lls = len(ls)
    for ils in range(lls):
        if ls[ils].startswith('"'):
            ls[ils] = ls[ils].strip('"')

    # 2020-11-17 20201117 17:30 1730
    # 0123456789 01234567 01234 0123

    dc = ls[0]
    if dc.endswith("00"):
        return

    ls[0] = ls[0][:4] + "-" + ls[0][4:6] + "-" + ls[0][6:8]
    if len(ls[1]) > 2:
        ls[1] = ls[1][:2] + ":" + ls[1][2:4]
    else:
        ls[1] = ls[1][:2] + ":00"

    if ls[2] == "Санкт-Петербург":
        ls[2] = "СПб"

    if ls[2] in cit2:
        ls[2] = "СПб"

    if ls[2] != "СПб":
        for beg in cit1:
            if ls[2].startswith(beg):
                break
        else:
            ls = ls[:2] + ["СПб"] + ls[2:]

    ls[2] = ls[2].strip('",.')
    if ls[2].startswith("г."):
        ls[2] = ls[2][2:]

    if lls>=9:
        ls[8] += rem
    elif lls>=6:
        ls[5] += rem
    elif lls >= 5:
        ls.append(rem)

    ls.append("")
    ls.append("")
    ls.append("")
    ls.append("")
    ls.append("")
    ls.append("")

    ls[5] += f"{ls[6]} {ls[7]} {ls[8]}"
    ls[5] = ls[5].strip("")

    status = getstatus(ls[5])
    shown = 'shown'

    wd = getwd(ls[0])
    dtuser = dc[6:] + "." + dc[4:6] + "." + dc[0:4]

    ls = [wd] + [dtuser] + ls
    ls = ls[:9] + [status] + [shown]

    ol = "\t".join(ls)
    ol = ol.rstrip("\t")
    outf.write (ol + "\n")
    outs = ""
    rem = ""
    state = 0


def getstatus(s):
    """ показать статус: было, будет, отмена, замена, перенос, прочее """
    """ ok plan cancel change shift etc """

    st = "ok"
    ss = s.lower()
    if "отмен" in ss:
        st = "cancel"
    elif "перенос" in ss or "перенес" in ss:
        st = "shift"
    elif "замен" in ss:
        st = "change"

    return st


def getwd(ds):
    """ получить день недели """

    # ~ if ds.endswith("00"):
        # ~ ds = ds[:-2] + "01"
    d = date.fromisoformat(ds)
    wd = d.weekday()
    week = "пн вт ср чт пт сб вс".split()
    return week[wd]

print ("starting...")

state = 0

with open (infile) as inf, open (outfile, 'w') as outf:
    #outf.write('DATE TIME    CITY    PLACE   PERSON  DESC    ADDRESS PRICE   REM SOURCE\n')
    #           0    1       2       3       4       5       6       7       8   9
    outf.write('wd  date    datesql time    city    place   what    desc    source  status  shown\n')
    #            0  1    2       3    4    5     6    7    8

    ln = 0
    outs = ""
    rem = ""

    for aline in inf:

        ln += 1
        print (ln, end=", ")

        line = aline.strip()
        # ~ print (line)
        if len(line) == 0:
            continue

        if line.startswith ('DATE'):
            if state and outs:
                tofile (outs)
            continue

        if line.startswith ("199") or line.startswith ("200"):
            if state and outs:
                tofile (outs)
            outs = line
            state = 1
            rem = ""

        else:
            line = line.strip("'")
            line = line.strip('"')
            rem += line

    if state:
        tofile (outs)

print ("finished.")

# ~ оставлены на последующую обработку
# ~ ляпы типа двойных кавычек (много) в "местах",
# ~ пустые поля "источников", и при этом они записаны как "От такого-то"
# ~ (иногда в [скобках], иногда в им.п., или в род.п.)
