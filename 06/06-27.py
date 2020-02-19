#docx檔案題庫包含很多段，每段一個題目，格式為：問題。（答案）
#資料庫datase.db中，tiku資料表包含kechengmingcheng,zhangjie,timu,daan四個欄位
#資料庫有關知識，請查看本書第8章
import sqlite3
from docx import Document

doc = Document('《Python程式設計》題庫.docx')

#連接資料庫
conn = sqlite3.connect('database.db')
cur = conn.cursor()

#先清空原來的題庫，可省略
cur.execute('delete from tiku')
conn.commit()

for p in doc.paragraphs:
    text = p.text
    if '（' in text and '）' in text:
        index = text.index('（')
        #分離問題和答案
        question = text[:index]
        if '___' in question:
            question = '填空題：' + question
        else:
            question = '判斷題：' + question
        answer = text[index+1:-1]
        #將資料寫入資料庫
        sql = 'insert into tiku(kechengmingcheng,zhangjie,timu,daan) values("Python程式設計","未分類","'+question+'","'+answer+'")'
        cur.execute(sql)
conn.commit()
#關閉資料庫連接
conn.close()
