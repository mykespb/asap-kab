#!/usr/bin/env python
# myke 2022-05-16 2022-05-16 0.1.4
# proc-pass-01.py 

# ~ обработка файлов архивов событий pass-YYYY.par
# ~ вер. 0.1 - просто проверка доступа

import glob
import re

print("\nсписок файлов с архивами")
lof = glob.glob('pass-*.par')
print(lof)

# ~ обработка 1 файла
fp = lof[0]
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
events = re.search('newitemsee\[(.*)\]', text)
ev = events.group(0)
print(ev)

# обрабатываем 1 событие
ev = ev.replace(r'\;', '!SEPA')
name, data, desc = ev.split(';', 2)
name = name.replace('newitemsee[', '')
desc = desc.replace("!SEPA", ";")
desc = re.sub(r'\^toperson\[[^\]]*\;([^\]]*)\]', r'\1', desc)
desc = desc.replace("[", "").replace("]", "")
desc = desc.strip()

print(f"\n1 событие:\n{name=}\n{data=}\n{desc=}\n")

# ~ пока что так:

# ~ список файлов с архивами
# ~ ['pass-2008.par', 'pass-2009.par', 'pass-2010.par', 'pass-2011.par', 'pass-2012.par', 'pass-2013.par', 'pass-2014.par', 'pass-2015.par', 'pass-2016.par', 'pass-2017.par', 'pass-2018.par', 'pass-2019.par', 'pass-2020.par', 'pass-2021.par']

# ~ обрабатываем архив pass-2008.par

# ~ newitemsee[29.12.2008 - Клубный вечер 19:00;2008-12-29; <a href=http://www.club-chetverg.narod.ru/ target=etc>Клуб  &laquo^;Четверг&raquo^;:</a> Александр Бутягин, Татьяна Землеруб, Дарья Зуева, ^toperson[kolomensky-de;Дмитрий Коломенский], Елена Максимова, Татьяна Черкасская. ]

# ~ 1 событие:
# ~ name='29.12.2008 - Клубный вечер 19:00'
# ~ data='2008-12-29'
# ~ desc='<a href=http://www.club-chetverg.narod.ru/ target=etc>Клуб  &laquo^;Четверг&raquo^;:</a> Александр Бутягин, Татьяна Землеруб, Дарья Зуева, Дмитрий Коломенский, Елена Максимова, Татьяна Черкасская.'
