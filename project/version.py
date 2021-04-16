import sqlite3 as lite
import sys
con = lite.connect('test.db')

cur = con.cursor()
cur.execute('SELECT SQLITE_VERSION()')

data = cur.fetchone()[0]

print ("SQLite version: {}".format(data))

print ("Error {}:".format(e.args[0]))

