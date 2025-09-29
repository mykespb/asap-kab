#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2025-09-28 2025-09-28 1.0
# find-bad-chars.py

# ~ Найти плохие ситмволы в именах файлов.

import glob, re

good = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя -_!?.,()[]\''

for fn in glob.glob('*.txt'):
    for c in fn:
        if c not in good:
            print(c, fn)
            break

