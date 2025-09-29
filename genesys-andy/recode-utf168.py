#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2025-09-28 2025-09-28 1.0
# recode-utf168.py

# ~ 1 попытка перекодировать содержимое файлов генезисов Энди Иванова.
# ~ В именах файлов есть проблемные спецсимволы.
# ~ КОдировка файлов, _в основном_, UTF16,
# ~ но есть и другие (UTF6, неопознанные
# ~ (размер выходного файла в таких случаях равен 0)).

import os

dir_in   = '/in'
dir_out  = '/out'
file_pat = '*.txt'
enc_in   = 'utf16'
enc_out  = 'utf8'

for (root, dirs, files) in os.walk(os.getcwd() + dir_in):
    print(f"{root=}, {dirs=}, {files=}")

    for afile in files:
        in_name = root + '/' + afile
        out_name = root[:-2] + 'out' + '/' + afile
        print(f"{in_name=}, {out_name=}")

        try:
            with open(in_name, encoding=enc_in, mode='r') as fr, \
                open(out_name, encoding=enc_out, mode='w') as fw:
                txt = fr.read()
                fw.write(txt)
        except Exception as e:
            print(f"Bad encoding")
            try:
                with open(in_name, encoding=enc_out, mode='r') as fr, \
                    open(out_name, encoding=enc_out, mode='w') as fw:
                    txt = fr.read()
                    fw.write(txt)
            except:
                print("Again bad excoding")
            


# ~ for (root, dirs, files) in os.walk(os.getcwd() + dir_in):
    # ~ print("Directory path: %s"%root)
    # ~ print("Directory Names: %s"%dirs)
    # ~ print("Files Names: %s"%files)
    
