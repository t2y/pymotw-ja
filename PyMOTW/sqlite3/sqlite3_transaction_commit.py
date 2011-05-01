#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Creating the schema in an sqlite3 database.
"""
#end_pymotw_header

import sqlite3

db_filename = 'todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select name, description from project')
    for name, desc in cursor.fetchall():
        print '  ', name
    return

with sqlite3.connect(db_filename) as conn1:

    print 'Before changes:'
    show_projects(conn1)

    # あるカーソルで追加する
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into project (name, description, deadline)
    values ('virtualenvwrapper', 'Virtualenv Extensions', '2011-01-01')
    """)

    print '\nAfter changes in conn1:'
    show_projects(conn1)

    # 他のコネクションからコミットせずに選択する
    print '\nBefore commit:'
    with sqlite3.connect(db_filename) as conn2:
        show_projects(conn2)

    # コミットしてから他のコネクションで選択する
    conn1.commit()
    print '\nAfter commit:'
    with sqlite3.connect(db_filename) as conn3:
        show_projects(conn3)
    
