# Проект АСАП/КААП.
# преобразование описи архива Антонова к стандартному виду
# (С) )М.Колодин, 2020
# 2020-07-05 1.0

import csv
import os.path

infile = 'ff_antonov_songs.csv'
outfile = 'antonov.csv'

if os.path.isfile(infile):
    print (f"file {infile} exists")
else:
    print (f"file {infile} does not exist")

with open (infile) as inf, open (outfile, 'w') as outf:
    reader = csv.reader (inf, delimiter="\t")
    writer = csv.writer (outf, delimiter="\t")
    headers = next (reader)
    print (headers)
    writer.writerow (["number", "song_author", "song_name", "song_line1"])

    count = 0
    for row in reader:

        if row[0] != '' and row[1] != "":
            # новый автор
            author = row[1]
            continue

        if row[0] == '' and row[1] != '':
            # буквы автора
            continue

        if row[0] == '' and row[1] == '' and row[2] == '':
            # пустая строка
            continue

        if row[0] == '27506':
            # пустая строка
            continue

        count += 1
        outrow = [count, author, row[2], row[3]]
        print (outrow)
        writer.writerow (outrow)

#        if count>=100: break
