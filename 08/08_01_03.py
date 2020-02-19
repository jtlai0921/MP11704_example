import sqlite3

conn = sqlite3.connect("D:\\test.db")
c = conn.cursor()
#c.execute('''create table stocks(date text, trans text, symbol text, qty real, price real)''')
c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")
conn.commit()

conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('select * from stocks')
r = c.fetchone()
print(type(r))
print(tuple(r))
print(r[2])
print(r.keys())
print(r['qty'])
for field in r:
    print(field)

c.close()
