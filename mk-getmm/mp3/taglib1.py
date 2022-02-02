#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-02 2022-02-02 1.1
# taglib1.py
# ~ проверка вынимания информации из аудиофайлов

# ~ https://github.com/supermihi/pytaglib
# ~ https://github.com/supermihi/pytaglib/blob/main/src/taglib.pyx
# ~ https://en.wikipedia.org/wiki/ID3

import taglib as tl
import glob

infiles = glob.glob("*.mp3")

print (f"working with {infiles}")

for mp3 in infiles:
    print(f"\nfile: {mp3}")
    audio = tl.File(mp3)
    print (f"{audio.tags=}")
    print (f"{audio.length=}")
    print (f"{audio.bitrate=}")
    print (f"{audio.sampleRate=}")
    print (f"{audio.channels=}")
    print (f"{audio.readOnly=}")

    
# ~ working with ['VH01LP01.mp3', 'kozlovsky-x1.mp3', 'kim-malchik.mp3', 'dolsky-x1.mp3', 'kim-gercogina.mp3']

# ~ file: VH01LP01.mp3
# ~ audio.tags={'ALBUM': ['"ß áû ñêàçàë òåáå ìíîãî õîðî'], 'ARTIST': ['[Âèõîðåâ]'], 'COMMENT': ['Mikel Lavrentyev archive'], 'TITLE': ['ß áû ñêàçàë òåáå ìíîãî õîðîøåã'], 'TRACKNUMBER': ['1']}
# ~ audio.length=117
# ~ audio.bitrate=256
# ~ audio.sampleRate=44100
# ~ audio.channels=2
# ~ audio.readOnly=False

# ~ file: kozlovsky-x1.mp3
# ~ audio.tags={'ALBUM': ['Ìîÿ ïåñíÿ íà êîìïàêòå'], 'ARTIST': ['Àíäðåé Êîçëîâñêèé'], 'COMMENT': ['                              '], 'DATE': ['1996'], 'TITLE': ['Çàñòîëüíàÿ (pàññêàç î ó÷åáå)']}
# ~ audio.length=27
# ~ audio.bitrate=128
# ~ audio.sampleRate=44100
# ~ audio.channels=2
# ~ audio.readOnly=False

# ~ file: kim-malchik.mp3
# ~ audio.tags={'ALBUM': ['Лучшие песни'], 'ALBUMARTIST': ['юлий ким'], 'ARTIST': ['Юлий Ким'], 'COMPOSER': ['В. Дашкевич'], 'GENRE': ['Разное'], 'LENGTH': ['141413'], 'TITLE': ['Куда ты скачешь, мальчик...'], 'TRACKNUMBER': ['31']}
# ~ audio.length=141
# ~ audio.bitrate=128
# ~ audio.sampleRate=44100
# ~ audio.channels=2
# ~ audio.readOnly=False

# ~ file: dolsky-x1.mp3
# ~ audio.tags={'ALBUM': ['C62 13067 Ïåñíè'], 'ARTIST': ['Äîëüñêèé Àëåêñàíäð'], 'COMMENT': ['èç àðõèâà alexey@mamarin.ru'], 'ENCODING': ['LAME v3.98 (alpha)'], 'LENGTH': ['0'], 'TITLE': ['Áëþç äëÿ òðóáû è ñåðäöà (Ïàìÿòè Ëóè Àðìñòðîíãà)'], 'TRACKNUMBER': ['1']}
# ~ audio.length=229
# ~ audio.bitrate=126
# ~ audio.sampleRate=44100
# ~ audio.channels=2
# ~ audio.readOnly=False

# ~ file: kim-gercogina.mp3
# ~ audio.tags={'ALBUM': ['Ãóáû îêàÿííûå'], 'ARTIST': ['Þëèé Êèì'], 'DATE': ['1994'], 'GENRE': ['Other'], 'TITLE': ['Ãåðöîãèíÿ']}
# ~ audio.length=135
# ~ audio.bitrate=128
# ~ audio.sampleRate=48000
# ~ audio.channels=1
# ~ audio.readOnly=False
