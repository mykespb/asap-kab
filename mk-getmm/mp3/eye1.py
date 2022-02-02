#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-02 2022-02-02 1.2
# eye1.py
# ~ проверка вынимания информации из аудиофайлов

# ~ https://eyed3.readthedocs.io/en/latest/
# ~ https://en.wikipedia.org/wiki/ID3

import eyed3 as eye
import glob

# ~ infiles = 'kim-gercogina.mp3  kim-malchik.mp3' . split()
infiles = glob.glob("*.mp3")

print (f"работаем с {infiles}")

for mp3 in infiles:
    print(f"\nfile: {mp3}")
    audio = eye.load(mp3)
    try:
        print (f"{audio.tag.title=}")
    except:
        print ("no tag title")
    try:
        print (f"{audio.tag.artist=}")
    except:
        print ("no tag artist")
    try:
        print (f"{audio.tag.album=}")
    except:
        print ("no tag album")
    try:
        print (f"{audio.tag.year=}")
    except:
        print ("no tag year")
    try:
        print (f"{audio.tag.comment=}")
    except:
        print ("no tag comment")
    try:
        print (f"{audio.tag.track=}")
    except:
        print ("no tag track")
    try:
        print (f"{audio.tag.genre.values=}")
    except:
        print ("no tag genre")

# ~ работаем с ['VH01LP01.mp3', 'kozlovsky-x1.mp3', 'kim-malchik.mp3', 'dolsky-x1.mp3', 'kim-gercogina.mp3']

# ~ file: VH01LP01.mp3
# ~ Invalid numeric genre ID: 255
# ~ Unknown genre ID: 255
# ~ audio.tag.title='ß áû ñêàçàë òåáå ìíîãî õîðîøåã'
# ~ audio.tag.artist='[Âèõîðåâ]'
# ~ audio.tag.album='"ß áû ñêàçàë òåáå ìíîãî õîðî'
# ~ no tag year
# ~ no tag comment
# ~ no tag track
# ~ no tag genre

# ~ file: kozlovsky-x1.mp3
# ~ Invalid numeric genre ID: 255
# ~ Unknown genre ID: 255
# ~ audio.tag.title='Çàñòîëüíàÿ (pàññêàç î ó÷åáå)'
# ~ audio.tag.artist='Àíäðåé Êîçëîâñêèé'
# ~ audio.tag.album='Ìîÿ ïåñíÿ íà êîìïàêòå'
# ~ no tag year
# ~ no tag comment
# ~ no tag track
# ~ no tag genre

# ~ file: kim-malchik.mp3
# ~ audio.tag.title='Куда ты скачешь, мальчик...'
# ~ audio.tag.artist='Юлий Ким'
# ~ audio.tag.album='Лучшие песни'
# ~ no tag year
# ~ no tag comment
# ~ no tag track
# ~ Non standard genre name: Разное
# ~ no tag genre

# ~ file: dolsky-x1.mp3
# ~ audio.tag.title='Áëþç äëÿ òðóáû è ñåðäöà (Ïàìÿòè Ëóè Àðìñòðîíãà)'
# ~ audio.tag.artist='Äîëüñêèé Àëåêñàíäð'
# ~ audio.tag.album='C62 13067 Ïåñíè'
# ~ no tag year
# ~ no tag comment
# ~ no tag track
# ~ no tag genre

# ~ file: kim-gercogina.mp3
# ~ audio.tag.title='Ãåðöîãèíÿ'
# ~ audio.tag.artist='Þëèé Êèì'
# ~ audio.tag.album='Ãóáû îêàÿííûå'
# ~ no tag year
# ~ no tag comment
# ~ no tag track
# ~ no tag genre
