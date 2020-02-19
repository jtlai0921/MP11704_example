import sqlite3

#自訂反覆運算器，按順序產生小寫字母
class IterChars:
    def __init__(self):
        self.count = ord('a')
    def __iter__(self):
        return self
    def __next__(self):
        if self.count > ord('z'):
            raise StopIteration
        self.count += 1
        return (chr(self.count - 1),)

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table characters(c)")
#建立反覆運算器物件
theIter = IterChars()
#插入記錄，每次插入一個英文小寫字母
cur.executemany("insert into characters(c) values (?)", theIter)
#讀取並顯示所有記錄
cur.execute("select c from characters")
print(cur.fetchall())
