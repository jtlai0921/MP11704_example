import sqlite3
import string

#包含yield語句的函數，可用來建立產生器物件
def char_generator():
    for c in string.ascii_lowercase:
        yield (c,)

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table characters(c)")
#使用產生器物件得到參數列表
cur.executemany("insert into characters(c) values (?)", char_generator())
cur.execute("select c from characters")
print(cur.fetchall())
