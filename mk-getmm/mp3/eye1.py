#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-02 2022-02-02 0.1
# eye1.py
# ~ проверка вынимания информации из аудиофайлов

import eyed3 as eye

infiles = 'kim-gercogina.mp3  kim-malchik.mp3' . split()

print (f"работаем с {infiles}")

for mp3 in infiles:
    print(mp3)
    audio = eye.load(mp3)
    print (audio.tag.title)
