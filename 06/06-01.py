s = 'Hello world\n文字檔的讀取方法\n文字檔的寫入方法\n'
with open('sample.txt', 'a+') as f:
      f.write(s)
