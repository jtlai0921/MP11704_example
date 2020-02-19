from PIL import Image
import os

gifFileName = 'bike.gif'
#以Image模組的open()方法開啟gif動態圖形時，預設是第一幀
im = Image.open(gifFileName)
pngDir = gifFileName[:-4]
#建立存放每幀圖片的資料夾
os.mkdir(pngDir)

try:
    while True:
        #儲存目前幀圖片
        current = im.tell()
        im.save(pngDir+'\\'+str(current)+'.png')
        #取得下一幀圖片
        im.seek(current+1)
except EOFError:
    pass
