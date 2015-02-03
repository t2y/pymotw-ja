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

with sqlite3.connect(db_filename) as conn:

    print 'Before changes:'
    show_projects(conn)

    try:

        # 削除
        cursor = conn.cursor()
        cursor.execute("delete from project where name = 'virtualenvwrapper'")

        # 設定を表示する
        print '\nAfter delete:'
        show_projects(conn)

        # 処理がエラーを引き起こしたように見せかける
        raise RuntimeError('simulated error')

    except Exception, err:
        # 変更を放棄する
        print 'ERROR:', err
        conn.rollback()
        
    else:
        # 変更を保存する
        conn.commit()

    # 結果を表示する
    print '\nAfter rollback:'
    show_projects(conn)
