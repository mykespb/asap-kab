#!/usr/bin/env python
# myke 2022-05-16 2022-05-16 0.3.1
# proc-pass-03.py 

# ~ обработка файлов архивов событий pass-YYYY.par
# ~ вер. 0.3 - полный просмотр всех текстов, 
# ~ перебор всех событий,
# ~ но пока без баз данных

import glob
import re

def proc_all_files(lof):
    print("\n=================== обработка всего =====================")
    
    for afile in lof:
        print(f"\n--------------- файл {afile} -------------------")
        proc_file(afile)
        
def proc_file(name):
    """обработать 1 файл"""
    global all_events

    # ~ обработка 1 файла
    fp = name
    # потом будет цикл по всем файлам
    print(f"\nобрабатываем архив {fp}\n")

    # открываем 1ый файл
    with open(fp, encoding="utf8") as fin:
        text = fin.read()

    # делаем замены для поабзацной обработки
    text = text.replace("\s", " ").replace("\t", " ")
    text = text.replace("\n\n", "!ABZAC")
    text = text.replace("\n", " ")
    text = text.replace("!ABZAC", "\n\n")

    # находим все события
    cur_event = 0
    for event in re.finditer('newitemsee\[(.*)\]', text):
        cur_event += 1
        all_events += 1
        proc_event(event.group(0), event.start(), event.end(), cur_event, all_events)

    # ~ print(f"всего нашли событий: {all_events}\n")
    
def proc_event(event, startt, end, cur, num):
    """обработать 1 событие"""

    event = event.replace(r'\;', '!SEPA')
    name, data, desc = event.split(';', 2)
    name = name.replace('newitemsee[', '')
    desc = desc.replace("!SEPA", ";")
    desc = re.sub(r'\^toperson\[[^\]]*\;([^\]]*)\]', r'\1', desc)
    desc = desc.replace("[", "").replace("]", "")
    desc = desc.strip()

    print(f"\nсобытие {cur} / {num}:\n{name=}\n{data=}\n{desc=}\n")

all_files = all_events = 0

print("\nсписок файлов с архивами")
lof = glob.glob('pass-*.par')
print(lof)
all_files += len(lof)

proc_all_files(lof)

print(f"""
=========================================================

всего обработано:
файлов:  {all_files:5}
событий: {all_events:5}

=========================================================
""")

# ~ пока так:
    
