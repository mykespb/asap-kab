#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-03 2022-02-03 1.1
# tinytag2.py
# ~ проверка вынимания информации из видеофайлов
# ~ https://pythonrepo.com/repo/devsnd-tinytag-python-audio
# ~ https://en.wikipedia.org/wiki/ID3

import glob
from tinytag import TinyTag

infiles = glob.glob("*.mp4")

print (f"working with {infiles}")

for mp4 in infiles:
    print(f"\nfile: {mp4}")
    audio = TinyTag.get(mp4)
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

# ~ working with ['kozlovsky-yaikot.mp4', 'msch-galichu.mp4', 'dikshtejn-osenj.mp4']

# ~ file: kozlovsky-yaikot.mp4
# ~ audio.album=None
# ~ audio.albumartist=None
# ~ audio.artist=None
# ~ audio.audio_offset=None
# ~ audio.bitrate=303038.464
# ~ audio.comment=None
# ~ audio.composer=None
# ~ audio.disc=None
# ~ audio.disc_total=None
# ~ audio.duration=176.12333333333333
# ~ audio.filesize=7927683
# ~ audio.genre=None
# ~ audio.samplerate=44100
# ~ audio.title=None
# ~ audio.track=None
# ~ audio.track_total=None
# ~ audio.year=None

# ~ file: msch-galichu.mp4
# ~ audio.album=None
# ~ audio.albumartist=None
# ~ audio.artist=None
# ~ audio.audio_offset=None
# ~ audio.bitrate=303038.464
# ~ audio.comment=None
# ~ audio.composer=None
# ~ audio.disc=None
# ~ audio.disc_total=None
# ~ audio.duration=168.29666666666665
# ~ audio.filesize=2672138
# ~ audio.genre=None
# ~ audio.samplerate=44100
# ~ audio.title=None
# ~ audio.track=None
# ~ audio.track_total=None
# ~ audio.year=None

# ~ file: dikshtejn-osenj.mp4
# ~ audio.album=None
# ~ audio.albumartist=None
# ~ audio.artist=None
# ~ audio.audio_offset=None
# ~ audio.bitrate=303038.464
# ~ audio.comment=None
# ~ audio.composer=None
# ~ audio.disc=None
# ~ audio.disc_total=None
# ~ audio.duration=159.28833333333333
# ~ audio.filesize=6926065
# ~ audio.genre=None
# ~ audio.samplerate=44100
# ~ audio.title=None
# ~ audio.track=None
# ~ audio.track_total=None
# ~ audio.year=None
