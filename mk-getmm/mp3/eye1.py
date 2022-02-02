#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-02 2022-02-02 1.1
# eye1.py
# ~ проверка вынимания информации из аудиофайлов

# ~ https://eyed3.readthedocs.io/en/latest/
# ~ https://en.wikipedia.org/wiki/ID3

import eyed3 as eye

infiles = 'kim-gercogina.mp3  kim-malchik.mp3' . split()

print (f"работаем с {infiles}")

for mp3 in infiles:
    print(mp3)
    audio = eye.load(mp3)
    try:
        print (audio.tag.title)
    except:
        print ("no tag title")
    try:
        print (audio.tag.artist)
    except:
        print ("no tag artist")
    try:
        print (audio.tag.album)
    except:
        print ("no tag album")
    try:
        print (audio.tag.year)
    except:
        print ("no tag year")
    try:
        print (audio.tag.comment)
    except:
        print ("no tag comment")
    try:
        print (audio.tag.track)
    except:
        print ("no tag track")
    try:
        print (audio.tag.genre)
    except:
        print ("no tag genre")

# ~ работаем с ['kim-gercogina.mp3', 'kim-malchik.mp3']
# ~ kim-gercogina.mp3
# ~ Ãåðöîãèíÿ
# ~ Þëèé Êèì
# ~ Ãóáû îêàÿííûå
# ~ no tag year
# ~ no tag comment
# ~ no tag track
# ~ (12)Other
# ~ kim-malchik.mp3
# ~ Куда ты скачешь, мальчик...
# ~ Юлий Ким
# ~ Лучшие песни
# ~ no tag year
# ~ no tag comment
# ~ no tag track
# ~ Non standard genre name: Разное
# ~ Разное
