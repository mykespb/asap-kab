События АП -- подход 2021
==========================================

Новый подход с расширениями на ВБА и Описи
------------------------------------------

Автор: Михаил Колодин

Дата начала: 2021-01-01

Дата правки: 2021-04-24

Версия: 1.4

Задача
------------------------------------------

Разработать и создать 
полный целостный пополняемый распределённый развиваемый
архив-афишу событий авторской песни.

Решение
------------------------------------------

### Этап 1

2021-04-23

Получить данные с сайта БА-СПб -- ОК

### Этап 2

2021-04-24

Объединить с имеющимися историческими данными. -- OK

Объединить колонки по максимальному набору.
Добавить uuid.

### Этап 3

Почистить результат,

Переделать datesql в dtsql, включив туда и время.

Учесть отмены концертов. -- 29 раз

Чистим:
- редактором БД
- питоном
- ручной правкой (лучше нет).

Выкладывание проекта на github.

### Этап 4

Правка структуры БД на перспективу

Добавление столбцов про тип события,
Добавление столбца про жанр события,
Правка столбца про статус,
Правка столбца про видимость:
Добавление столбцов про организацию и ведущих.
Добавить в БД таблицы и столбцы оргов и т.п.
Обработать данные, получив дополнительные сведения о ценах, оргах, местах и т.п.
Добавить столбцы в json:
- jsonafter json -- параметры события (ведущий, цены, число зрителей, кто и какие делал записи, фото, и т.п.)
- jsonrefs json -- ссылки на сетевые ресурсы (самого концерта, метасобытия. оргов, клубов, страниц рекламы и т.п., по возможности.  с описаниями и точно - с указанием типа ссылки (на событие, на рекламу, на орга, прочее непонятное встреченное)) 
- jsonetc josn -- всё прочее, что можно извлечь по данным, указанным человеком
- jsonnotes json -- все примечания. оставленнеые редакторами
  [{person: "id/uuid", dtcre: "iso", dtmod: "iso", note: "text", uuid: "uuid of note"}]
- jsonauto json -- всё, что автоматически найдёт и заполнит робот

### Этап 5

Многоредакторский сайт

Добавить в БД столбец "дата-время последней правки", "кто правил".
Полноценные данные о редакторах сайта - в отдельной таблице.
Более сложный парольный вход.

Таблица с логами, ротация логов по крону,

Возможность отката некоторых правок.

Взаимодействие ведущих, админов, информацторов:
чат на сайте, сайтовая почта, взаимные блокноты.

Блокноты самих ведущих -- для себя.

Сообщение между ведущими и админом -- персонально.

Новости системы:

Проработка расределённой системы,
со многими сайтами, админами, ведущими, оргами.

Взаимодействие с оргами, переписка, напоминания, запросы, уточнения.

### Этап 6

Подготовка к статусу - формату ВБА

Добавление колонок про географию.

Добавить в БД таблицы и столбцы географии и пр. юридические, географические, административные, временные сведения для полуавтоматической обработки.
Провести автообработку.

### Этап 7

Подготовить и провести автообработку.

Добавить в БД таблицы и столбцы для автообработки -- способ получения информации, достоверность, программа, версия и т.п.
Провести автообработку.

### Этап 8

Добавить архивные, исторические данные (после переформатирования и обработки): 

- сайт Востока
- архивы ВБА
- архивы Доброхота
- ...

### Этап 9

Взаимно подготовить сайт и архив.

Подготовить БД к выкладыванию на сайт.
Подготовить новый сайт к выкладыванию данных.
Ввести административные меры,
создать ведущих и прочих участников с различными ролями и правами,
ввести логи, их обработку.
Обеспечить связь информации о событиях, клубах, площадках, и т.п.

### Этап 10

Согласовать сайт и рассылку на subscribe.ru, 

подготовить txt и html версии рассылки,
причём многотабличные: 
собственно события, 
клубы и площадки, участвующие в этих событиях,
прочие материалы, с ними связанные,
а также общеполитические, общекультурные явления, 
санитарные правила, 
объявления свои и чужие,
ссылки на сайты и рассылки,
другая поезная информация.

### Этап 11

Выложить на гуглотаблицы и описание на гуглодоки.

дать ссылки и обсудитиь на форуме ЦАПа и т.п.

### Этап 12

Согласовать с Описями архивов архивистами. 

в т.ч. с Народными Описями.

### Этап 13

Организовать соместную работу сайта и Описей, сайтов ВБА и локальных БА,

большой API (взаимный).

### Этап 14

ППИ - Полезный пользовательский интерфейс: 

выдачи по запросам, умный поиск, аналитика, диаграммы, сводки и т.п.
переходы к мультимедийным материалам, 
связанным с событиями, авторами, исполнителями, клубами, организаторами, 
внешними событиями и т.п.

### Этап 15

Объединить сайт Событий (БардАфиши) с полным архивом (каталогом) авторов и т.п.

(расширенные избранные места с bards.ru, bard.ru и т.п.).


Реализация
------------------------------------------


...

Примечания
------------------------------------------

https://docs.python.org/3/library/sqlite3.html

https://github.com/rogerbinns/apsw

https://rogerbinns.github.io/apsw/pysqlite.html

https://sqlite-utils.datasette.io/en/stable/python-api.html#storing-json

https://www.sqlite.org/json1.html

https://www.fullstackpython.com/sqlite.html

https://chrisostrouchov.com/post/python_sqlite/

http://www.bard-afisha.spb.ru/

https://github.com/NixOS/nixpkgs/issues/66526
...