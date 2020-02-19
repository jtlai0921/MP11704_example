import sqlite3

conn=sqlite3.connect('D:/addressBook.db')
cur=conn.cursor()
cur.execute('select * from addressList')
li = cur.fetchall()			#返回所有查詢結果
for line in li:
    for item in line:
        print(item, end=' ')
    print()
conn.close()
