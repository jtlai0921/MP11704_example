import sqlite3

persons = [
    ("Hugo", "Boss"),
    ("Calvin", "Klein")
    ]
conn = sqlite3.connect(":memory:")
# 建立資料表
conn.execute("create table person(firstname, lastname)")
# 插入資料
conn.executemany("insert into person(firstname, lastname) values (?, ?)", persons)
# 顯示資料
for row in conn.execute("select firstname, lastname from person"):
    print(row)
print("I just deleted", conn.execute("delete from person").rowcount, "rows")
