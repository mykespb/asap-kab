#!/usr/bin/env python3
# Проект АСАП/КААП.
# преобразование описи архива Баранова к правильному виду, подход 1
# (С) )М.Колодин, 2020
# 2020-07-10 1.0

import csv
import os.path

#infile  = 'baranov0.csv'
#outfile = 'baranov1.csv'

infile  = 'baranov.csv'
outfile = 'baranovx.csv'

if os.path.isfile(infile):
    print (f"file {infile} exists")
else:
    print (f"file {infile} does not exist")

with open (infile) as inf, open (outfile, 'w') as outf:
    reader = csv.reader (inf, delimiter="\t")
    writer = csv.writer (outf, delimiter="\t")
    headers = next (reader)
    print (headers)
    writer.writerow (["number", "song_line1", "song_name", "date", "song_author", "verses_author", "record_code", "used_in", "rem_singer", "file_name", "archive_notes"])

    countin = 0
    countout = 0
    for inrow in reader:
        countin += 1
        print ("inrow:", countin, inrow)

        if inrow[0].startswith('#'):
            print ("line skipped as comment")
            continue
#        print (countout, inrow)

        rlen = len(inrow)
        print (f"rlen={rlen}")
        if rlen < 6 or inrow[5] == "":
            countout += 1
            print ("no info about records")
            outrow = [countout, *inrow]
            print ("out fast:", outrow)
            writer.writerow(outrow)
            continue
        else:
            print ("normal string")

#       for item in inrow[6].split('[ ,.]+'):
        codes = inrow[5]
        codes = codes.replace('.', ',')
        codes = codes.replace('O', '0')
        codes = codes.replace('О', '0')
        codes = codes.replace(' ', '')

        items = codes.split(',')
        print ("got items:", items)

        for item in items:
            it = item.strip()
            if it == "":
                continue

            rem_singer = ""
            if "и" in it:
                rem_singer = "исполняет не автор"

            file_name = ""
            archive_notes = ""
            if "Д" not in it and "П" not in it:
                oit = it.strip("и")
                try:
                    file_name = "mb" + ("{:03d}".format(int(oit)))
                    archive_notes = file_name
                except:
                    print ("bad letter!")

            years = inrow[2]
            # if years.endswith("г."):
                # years = years[:-2]
            # elif years.endswith("г"):
                # years = years[:-1]

            usedin = ""
            if rlen>6:
                usedin = inrow[6]

            countout += 1
            print ("out:", [countout, inrow[0], inrow[1], years, inrow[3], inrow[4], it, usedin, rem_singer, file_name, archive_notes])
            writer.writerow([countout, inrow[0], inrow[1], years, inrow[3], inrow[4], it, usedin, rem_singer, file_name, archive_notes])

