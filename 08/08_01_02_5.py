import sqlite3

conn = sqlite3.connect("D:/addressBook.db")
cur = conn.cursor()		#建立指標
#cur.execute("create table addressList (name , sex , phon , QQ , address)")

cur.execute('''insert into addressList(name , sex , phon , QQ , address) values('王小丫' ,  '女' ,  '13888997011' ,  '66735' ,  '北京市' )''')
cur.execute('''insert into addressList(name, sex, phon, QQ, address) values('李莉', '女', '15808066055', '675797', '天津市')''')
cur.execute('''insert into addressList(name, sex, phon, QQ, address) values('李星草', '男', '15912108090', '3232099', '昆明市')''')
conn.commit()			#提交交易，把資料寫入資料庫
conn.close()
