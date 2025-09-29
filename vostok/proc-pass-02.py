#!/usr/bin/env python
# myke 2022-05-16 2022-05-16 0.2.2
# proc-pass-02.py 

# ~ обработка файлов архивов событий pass-YYYY.par
# ~ вер. 0.2 - полный просмотр всех текстов, 
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
    # ~ events = re.search('newitemsee\[(.*)\]', text)
    events = re.findall('newitemsee\[(.*)\]', text)
    
    # ~ print(f"всего нашли событий: {events.lastindex}")
    lene = len(events)
    print(f"всего нашли событий: {lene}\n")
    all_events += lene
    
    # ~ ev = events.group(0)
    ev = events[0]
    print(ev)

    proc_event(ev)
    
def proc_event(ev):
    """обработать 1 событие"""

    # обрабатываем 1 событие
    ev = ev.replace(r'\;', '!SEPA')
    name, data, desc = ev.split(';', 2)
    name = name.replace('newitemsee[', '')
    desc = desc.replace("!SEPA", ";")
    desc = re.sub(r'\^toperson\[[^\]]*\;([^\]]*)\]', r'\1', desc)
    desc = desc.replace("[", "").replace("]", "")
    desc = desc.strip()

    print(f"\n1 событие:\n{name=}\n{data=}\n{desc=}\n")

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
    
# ~ список файлов с архивами
# ~ ['pass-2008.par', 'pass-2009.par', 'pass-2010.par', 'pass-2011.par', 'pass-2012.par', 'pass-2013.par', 'pass-2014.par', 'pass-2015.par', 'pass-2016.par', 'pass-2017.par', 'pass-2018.par', 'pass-2019.par', 'pass-2020.par', 'pass-2021.par']

# ~ =================== обработка всего =====================

# ~ --------------- файл pass-2021.par -------------------

# ~ обрабатываем архив pass-2021.par

# ~ всего нашли событий: 51

# ~ пн 27.12.2021 19:00 Дни рождения месяца и Новый год.;2021-12-27; Вход 100 р.

# ~ 1 событие:
# ~ name='пн 27.12.2021 19:00 Дни рождения месяца и Новый год.'
# ~ data='2021-12-27'
# ~ desc='Вход 100 р.'

# ~ =========================================================

# ~ всего обработано:
# ~ файлов:     14
# ~ событий:   802

# ~ =========================================================
