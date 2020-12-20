#! /usr/bin/env python3

# получение списка полезных папок из выдачи команды dir (ms windwos)
# Mikhail (myke) Kolodin, 2020
# 2020-12-20 1.0

fin  = "disks.txt"
fout = "disks-str.tab"

with open(fin) as fi, open(fout, 'w') as fo:
    state = 0

    fo.write("tomame\ttomserial\ttomdir\tdate\tfolder\n")

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
            tomserial = line[22:]
            continue

        if state == 0 and "Содержимое папки" in line:
            tomdir = line[21:]
            state = 1
            continue

        if state == 1 and "Содержимое папки" in line:
            break

        if state == 1 and "<DIR>" in line and line[36] != ".":
            folder = line[36:]
            adate = line[:10]
            fo.write(f"{tomname}\t{tomserial}\t{adate}\t{tomdir}\t{folder}\n")

