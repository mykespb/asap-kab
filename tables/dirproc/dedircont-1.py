#! /usr/bin/env python3

# получение списка мультимедийных файлов из выдачи команды dir (ms windwos)
# Mikhail (myke) Kolodin, 2020
# 2020-12-20 1.3

def main():
    fin  = "disks.txt"
    fout = "disks-cont.tab"
    n    = 0

    with open(fin) as fi, open(fout, 'w') as fo:
        state = 0

        fo.write("n\ttomame\ttomserial\tdate\tfolder\tsize\tmmedia\n")

        for lin in fi:
            print(".", end="")
            line = lin.strip()
            lens = len(line)

            if state == 0 and lens == 0:
                continue

            if state == 0 and "Том в устройстве" in line:
                tomname = line[32:]
                continue

            if state == 0 and "Серийный номер тома" in line:
                tomserial = line[21:]
                continue

            if state == 0 and "Содержимое папки" in line:
                tomdir = line[21:]
                state = 1
                continue

            if state == 1 and "Содержимое папки" in line:
                tomdir = line[21:]
                continue

            if state == 1 and (line.endswith(".mp3") 
                or line.endswith(".mp4")
                or line.endswith(".avi")
                or line.endswith(".ogg")
                or line.endswith(".ra")
                or line.endswith(".wma")
                or line.endswith(".m4a")
                or line.endswith(".ad")
                or line.endswith(".aac")
                or line.endswith(".flac")
                ):
                n += 1
                folder = line[36:]
                adate = line[:10]
                ssize = line[18:35]
                ssize = ssize.strip()
                # ssize = ssize.translate(str.maketrans(dict.fromkeys(' \t\r\n')))
                # ssize = ssize.translate({ord(" "): ""})
                # ssize = ssize.translate(str.maketrans('', '', ' \t\n\r'))
                # ssize = ssize.replace(" ", "_")
                # ssize = int(ssize, 0)
                ssize = onlydigits(ssize)
                fo.write(f"{n}\t{tomname}\t{tomserial}\t{adate}\t{tomdir}\t{ssize}\t{folder}\n")

def onlydigits(s):
    """ leave only digits """
    r = ""
    for c in s:
        if c in "0123456789":
            r += c
    return r

main()