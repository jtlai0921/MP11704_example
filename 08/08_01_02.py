import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table people (name_last, age)")
who = "Dong"
age = 38
# 以問號作為預留位置
cur.execute("insert into people values (?, ?)", (who, age))
# 以命名變數作為預留位置
cur.execute("select * from people where name_last=:who and age=:age", 
          {"who": who, "age": age})
print(cur.fetchone())
