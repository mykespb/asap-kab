#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-09-29 2025-09-29 2.1
# make-site2.py

import os, os.path

rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
lat = "abvgdeezzijklmnoprstufhccsszyzeuaABVGDEEZZIJKLMNOPRSTUFHCCSSXYXEUA"

def this_dir(cdir):

    cwd = os.getcwd()
    print(f"working in {cwd=}")

    with open('index.html', 'w') as html:

        html.write(f"""<!DOCTYPE HTML>
<html lang='ru'>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<head>
<title>Andy Bards Genesys</title>
</head>

<body>
""")

        if os.path.exists('about.txt'):
            with open('about.txt', 'r') as about:
                txt = about.read()
                html.write(f"<h1>{txt}</h2>\n")

        html.write("\n<p>Каталоги</p>\n")

        files = os.listdir('.')

        alldirs = [f for f in files if not os.path.isfile(f) ]

        if alldirs:
            print(*alldirs)
            for adir in sorted(alldirs):
                html.write(f"<a href='{adir}'>{adir}</a><br>\n")
        else:
            print("no dirs")

        allfiles = [f for f in files if os.path.isfile(f) ]

        if allfiles:
            for adir in sorted(allfiles):
                html.write(f"<a href='{adir}'>{adir}</a><br>\n")
        else:
            print("no files")
        
        html.write("""
</body>
</html>
""")


cwd = os.getcwd()
print(f"working in {cwd=}")
this_dir('.')
