#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2025-09-29 2025-09-29 1.2
# rename-files-rus-eng.py

import os, os.path

rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
lat = "abvgdeezzijklmnoprstufhccssxyxeuaABVGDEEZZIJKLMNOPRSTUFHCCSSXYXEUA"


def ruseng(sin):

    sout = ''
    for c in sin:
        if (pos := rus.find(c)) != -1:
            sout += lat[pos]
        else:
            sout += c

    return sout


names = []

with open("index.html", 'w') as html:

    html.write("""<!DOCTYPE HTML>
<html lang='ru'>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<head>
<title>Andy Bards Genesys</title>
</head>

<body>
""")

    for from_file in os.listdir():
        if from_file in ('.', '..') or from_file.endswith('.py') or from_file == 'index.html':
            continue

        to_file = ruseng(from_file)

        print(f"{from_file} => {to_file}")
        os.rename(from_file, to_file)
        names.append((from_file, to_file))
        

    names.sort()

    for a, b in names:
        html.write(f"<a href='{b}'>{a[:-4]}</a><br>\n")
        print(f"<a href='{b}'>{a}</a><br>")

    html.write("""
</body>
</html>
""")
