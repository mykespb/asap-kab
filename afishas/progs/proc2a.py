#! /usr/bin/env python3
# Mikhail Kolodin, 2020
# proc2a.py 2020-11-17 1.3

# АСАП, КААП
# обработка бард-афиши 1998-2003 годов, архивист: М.Колодин

infile  = './ap2013.tabs'
outfile = './out-ap2013.tab'

print("starting...")
ln = 0

with open (infile) as inf, open (outfile, 'w') as outf:
    ln += 1
    print(ln, end=", ")
    outf.write('wd  date    datesql time    city    place   what    desc    source  status  shown\n')
    for aline in inf:
        line = aline.strip()
        line += "\tok\tshown\n"
        outf.write(line)

print("done.")
