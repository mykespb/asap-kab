#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-03 2022-02-03 1.1
# taglib2.py
# ~ проверка вынимания информации из видеофайлов

# ~ https://github.com/supermihi/pytaglib
# ~ https://github.com/supermihi/pytaglib/blob/main/src/taglib.pyx
# ~ https://en.wikipedia.org/wiki/ID3

import taglib as tl
import glob

infiles = glob.glob("*.mp4")

print (f"working with {infiles}")

for mp4 in infiles:
    print(f"\nfile: {mp4}")
    audio = tl.File(mp4)
    print (f"{audio.tags=}")
    print (f"{audio.length=}")
    print (f"{audio.bitrate=}")
    print (f"{audio.sampleRate=}")
    print (f"{audio.channels=}")
    print (f"{audio.readOnly=}")

# ~ working with ['kozlovsky-yaikot.mp4', 'msch-galichu.mp4', 'dikshtejn-osenj.mp4']

# ~ file: kozlovsky-yaikot.mp4
# ~ audio.tags={}
# ~ audio.length=176
# ~ audio.bitrate=96
# ~ audio.sampleRate=44100
# ~ audio.channels=2
# ~ audio.readOnly=False

# ~ file: msch-galichu.mp4
# ~ audio.tags={}
# ~ audio.length=168
# ~ audio.bitrate=96
# ~ audio.sampleRate=44100
# ~ audio.channels=2
# ~ audio.readOnly=False

# ~ file: dikshtejn-osenj.mp4
# ~ audio.tags={}
# ~ audio.length=159
# ~ audio.bitrate=96
# ~ audio.sampleRate=44100
# ~ audio.channels=2
# ~ audio.readOnly=False
