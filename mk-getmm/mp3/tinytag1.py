#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-02 2022-02-02 1.1
# tinyta1.py
# ~ проверка вынимания информации из аудиофайлов

# ~ https://pythonrepo.com/repo/devsnd-tinytag-python-audio
# ~ https://en.wikipedia.org/wiki/ID3

import glob
from tinytag import TinyTag

infiles = glob.glob("*.mp3")

print (f"working with {infiles}")

for mp3 in infiles:
    print(f"\nfile: {mp3}")
    audio = TinyTag.get(mp3)
    print (f"{audio.album=}")
    print (f"{audio.albumartist=}")
    print (f"{audio.artist=}")
    print (f"{audio.audio_offset=}")
    print (f"{audio.bitrate=}")
    print (f"{audio.comment=}")
    print (f"{audio.composer=}")
    print (f"{audio.disc=}")
    print (f"{audio.disc_total=}")
    print (f"{audio.duration=}")
    print (f"{audio.filesize=}")
    print (f"{audio.genre=}")
    print (f"{audio.samplerate=}")
    print (f"{audio.title=}")
    print (f"{audio.track=}")
    print (f"{audio.track_total=}")
    print (f"{audio.year=}")


# ~ working with ['VH01LP01.mp3', 'kozlovsky-x1.mp3', 'kim-malchik.mp3', 'dolsky-x1.mp3', 'kim-gercogina.mp3']

# ~ file: VH01LP01.mp3
# ~ audio.album='"ß áû ñêàçàë òåáå ìíîãî õîðî'
# ~ audio.albumartist=None
# ~ audio.artist='[Âèõîðåâ]'
# ~ audio.audio_offset=0
# ~ audio.bitrate=256
# ~ audio.comment='Mikel Lavrentyev archive'
# ~ audio.composer=None
# ~ audio.disc=None
# ~ audio.disc_total=None
# ~ audio.duration=117.28026331853633
# ~ audio.filesize=3752565
# ~ audio.genre=None
# ~ audio.samplerate=44100
# ~ audio.title='ß áû ñêàçàë òåáå ìíîãî õîðîøåã'
# ~ audio.track='1'
# ~ audio.track_total=None
# ~ audio.year=''

# ~ file: kozlovsky-x1.mp3
# ~ audio.album='Ìîÿ ïåñíÿ íà êîìïàêòå         '
# ~ audio.albumartist=None
# ~ audio.artist='Àíäðåé Êîçëîâñêèé             '
# ~ audio.audio_offset=0
# ~ audio.bitrate=128
# ~ audio.comment='                              '
# ~ audio.composer=None
# ~ audio.disc=None
# ~ audio.disc_total=None
# ~ audio.duration=27.451966533739935
# ~ audio.filesize=438982
# ~ audio.genre=None
# ~ audio.samplerate=44100
# ~ audio.title='Çàñòîëüíàÿ (pàññêàç î ó÷åáå)  '
# ~ audio.track=None
# ~ audio.track_total=None
# ~ audio.year='1996'

# ~ file: kim-malchik.mp3
# ~ audio.album='Лучшие песни'
# ~ audio.albumartist='юлий ким'
# ~ audio.artist='Юлий Ким'
# ~ audio.audio_offset=4608
# ~ audio.bitrate=128
# ~ audio.comment='                            '
# ~ audio.composer='В. Дашкевич'
# ~ audio.disc=None
# ~ audio.disc_total=None
# ~ audio.duration=141.34857142857143
# ~ audio.filesize=2261123
# ~ audio.genre='Разное'
# ~ audio.samplerate=44100
# ~ audio.title='Куда ты скачешь, мальчик...'
# ~ audio.track='31'
# ~ audio.track_total=None
# ~ audio.year=''

# ~ file: dolsky-x1.mp3
# ~ audio.album='C62 13067 Ïåñíè'
# ~ audio.albumartist=None
# ~ audio.artist='Äîëüñêèé Àëåêñàíäð'
# ~ audio.audio_offset=674
# ~ audio.bitrate=252
# ~ audio.comment='XXXèç àðõèâà alexey@mamarin.ru'
# ~ audio.composer=None
# ~ audio.disc=None
# ~ audio.disc_total=None
# ~ audio.duration=114.96489795918367
# ~ audio.filesize=3630480
# ~ audio.genre=None
# ~ audio.samplerate=44100
# ~ audio.title='Áëþç äëÿ òðóáû è ñåðäöà (Ïàìÿòè Ëóè Àðìñòðîíãà)'
# ~ audio.track='1'
# ~ audio.track_total=None
# ~ audio.year=''

# ~ file: kim-gercogina.mp3
# ~ audio.album='Ãóáû îêàÿííûå'
# ~ audio.albumartist=None
# ~ audio.artist='Þëèé Êèì'
# ~ audio.audio_offset=1792
# ~ audio.bitrate=128
# ~ audio.comment=''
# ~ audio.composer=None
# ~ audio.disc=None
# ~ audio.disc_total=None
# ~ audio.duration=135.696
# ~ audio.filesize=2173056
# ~ audio.genre='Other'
# ~ audio.samplerate=48000
# ~ audio.title='Ãåðöîãèíÿ'
# ~ audio.track=None
# ~ audio.track_total=None
# ~ audio.year='1994'
