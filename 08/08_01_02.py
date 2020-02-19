import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table people (name_last, age)")
who = "Dong"
age = 38
# �H�ݸ��@���w�d��m
cur.execute("insert into people values (?, ?)", (who, age))
# �H�R�W�ܼƧ@���w�d��m
cur.execute("select * from people where name_last=:who and age=:age", 
          {"who": who, "age": age})
print(cur.fetchone())
