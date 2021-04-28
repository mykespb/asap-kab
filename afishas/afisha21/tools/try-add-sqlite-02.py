#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  try-add-sqlite-01.py
#

import sqlite3
from sqlite_utils import Database

# ~ dbf = 'ap.json'

conn = sqlite3.connect(':memory:')
# ~ conn = sqlite3.connect()
conn.enable_load_extension(True)

db = Database(memory = True)

db['dogs'].insert( {'name': 'Fido','age': 30} )

print(db.table_names())

for row in db["dogs"].rows:
    print(row)

db["niche_museums"].insert({
    "name": "The Bigfoot Discovery Museum",
    "url": "http://bigfootdiscoveryproject.com/",
    "hours": {
        "Monday": [11, 18],
        "Wednesday": [11, 18],
        "Thursday": [11, 18],
        "Friday": [11, 18],
        "Saturday": [11, 18],
        "Sunday": [11, 18]
    },
    "address": {
        "streetAddress": "5497 Highway 9",
        "addressLocality": "Felton, CA",
        "postalCode": "95018"
    }
})

print(db.execute("""
    select json_extract(address, '$.addressLocality')
    from niche_museums
""").fetchall())



# ~ a = con.execute("pragma compile_options;")
# ~ for i in a:
    # ~ print(i); #check for ENABLE_JSON1

# ~ myke@mykem:~/bards/kab/2020/bard-afisha/2021/step03/test1$ ./try-add-sqlite-02.py
# ~ (u'COMPILER=gcc-9.3.0',)
# ~ (u'ENABLE_COLUMN_METADATA',)
# ~ (u'ENABLE_DBSTAT_VTAB',)
# ~ (u'ENABLE_FTS3',)
# ~ (u'ENABLE_FTS3_PARENTHESIS',)
# ~ (u'ENABLE_FTS3_TOKENIZER',)
# ~ (u'ENABLE_FTS4',)
# ~ (u'ENABLE_FTS5',)
# ~ (u'ENABLE_JSON1',)
# ~ (u'ENABLE_LOAD_EXTENSION',)
# ~ (u'ENABLE_PREUPDATE_HOOK',)
# ~ (u'ENABLE_RTREE',)
# ~ (u'ENABLE_SESSION',)
# ~ (u'ENABLE_STMTVTAB',)
# ~ (u'ENABLE_UNLOCK_NOTIFY',)
# ~ (u'ENABLE_UPDATE_DELETE_LIMIT',)
# ~ (u'HAVE_ISNAN',)
# ~ (u'LIKE_DOESNT_MATCH_BLOBS',)
# ~ (u'MAX_SCHEMA_RETRY=25',)
# ~ (u'MAX_VARIABLE_NUMBER=250000',)
# ~ (u'OMIT_LOOKASIDE',)
# ~ (u'SECURE_DELETE',)
# ~ (u'SOUNDEX',)
# ~ (u'TEMP_STORE=1',)
# ~ (u'THREADSAFE=1',)
# ~ (u'USE_URI',)


# ~ jsondbfile = 'ap.json'
# ~ conn = sqlite3.connect(jsondbfile)
# ~ cursor = conn.cursor()

# ~ sql = """ select
    # ~ json_extract(value, '$id') as myid,
    # ~ json_extract(value, '$date') as mydate
    # ~ from
    # ~ json_each(readfile(jsondbfile))
    # ~ """

# ~ cursor.execute(sql)

# ~ conn.close()

# ~ https://docs.python.org/3/library/sqlite3.html

# ~ https://github.com/rogerbinns/apsw

# ~ https://rogerbinns.github.io/apsw/pysqlite.html

# ~ https://sqlite-utils.datasette.io/en/stable/python-api.html#storing-json

# ~ https://www.sqlite.org/json1.html

# ~ https://www.fullstackpython.com/sqlite.html

# ~ https://chrisostrouchov.com/post/python_sqlite/

# ~ http://www.bard-afisha.spb.ru/
