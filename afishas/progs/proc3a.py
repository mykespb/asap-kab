#! /usr/bin/env python3
# Mikhail Kolodin, 2020
# proc3a.py 2020-11-17 0.1

# АСАП, КААП
# обработка бард-афиши 1998-2003 годов, архивист: М.Колодин

import sys
import re

infile  = sys.argv[1]
outfile = sys.argv[2]

def nodata():
    global wd, dt, dtsql, city, place, what, desc, source, state
    state = 0
    wd = ""
    dt = ""
    dtsql = ""
    city = ""
    place = ""
    what = ""
    desc = ""
    source = ""


print(f"\n-------------------------------\nstarting with files {infile} and {outfile}")

# 2020-11-17 20201117 17:30 1730 17.11.2020
# 0123456789 01234567 01234 0123 0123456789

nodata()
status = "ok"
shown = "shown"

with open(infile, 'r') as inf, open(outfile, 'w') as outf:

    state = 0

    outf.write('wd  date    datesql time    city    place   what    desc    source  status  shown\n')
    #            0  1       2       3       4       5       6       7       8       9       10

    for cnt, aline in enumerate(inf):
        print(cnt, end=", ")

        line = aline.strip()
        line = re.sub(r'\s+', ' ', line)
        if cnt < 5:
            print(line)

        if len(line) == 0:

            if state and wd:
                desc = desc.strip()
                source = source.strip()
                outf.write(f"{wd}\t{dt}\t{dtsql}\t{tm}\t{city}\t{place}\t{what}\t{desc}\t{source}\t{status}\t{shown}\n")
                nodata()
            continue

        if state == 0:
            wd, dt, tm, city, place = line.split(maxsplit=4)
            dtsql = dt[6:10] + "-"  + dt[3:5] + "-" + dt[0:2]
            if cnt < 30:
                print(f"X {wd}, {dt}, {dtsql}, {tm}, {city}, {place}")
            state = 1
            desc = ""
            source = ""
            continue

        if state == 1:
            what = line
            state = 2
            desc = ""
            source = ""
            continue

        if state == 2:
            if "источник" in line or "Источник" in line:
                state = 3
                source = ""
            else:
                desc += " " + line
                continue

        if state == 3:
            source += " " + line
            continue

    if state and wd:
        desc = desc.strip()
        source = source.strip()
        outf.write(f"{wd}\t{dt}\t{dtsql}\t{tm}\t{city}\t{place}\t{what}\t{desc}\t{source}\t{status}\t{shown}\n")

