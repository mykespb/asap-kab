#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-09-29 2025-09-29 1.0
# txt2html.py

# ~ Сконвертировать in/*.txt в out/*.html
# ~ проставив везде правильные заголовки html с кодировкой UTF8

import os

head = """<!DOCTYPE HTML>
<html lang='ru'>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<head>
<title>Andy Bards Genesys</title>
</head>

<body>
<pre>
"""

foot = """
</pre>
</body>
</html>
"""

nof = 0

for afile in os.listdir('in'):
    if not  afile.endswith('.txt'):
        continue

    nof += 1
    sfin  = 'in/' + afile
    sfout = 'out/' + afile[:-4] + '.html'

    with open(sfin, 'r') as fin, open(sfout, 'w') as fout:
        print(f"write from {sfin=}\n      to  {sfout=}")

        fout.write(head)

        txt = fin.read()

        fout.write(txt)

        fout.write(foot)

print(f'\n*** end of work, {nof} files processed')

