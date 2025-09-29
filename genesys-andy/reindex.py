#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-09-29 2025-09-29 1.0
# reindex.py

# ~ Перекодировать все ссылки в файле index.html так, чтобы вместо .txt были ссылки на .html

with open('in/index.html', 'r') as fin, open('out/index.html', 'w') as fout:

    txt = fin.read()
    txt = txt.replace('.txt', '.html')
    fout.write(txt)

