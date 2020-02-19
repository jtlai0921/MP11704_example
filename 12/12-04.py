from PIL import Image
import os

def searchLeft(width, height, im):
    for w in range(width):		#由左向右掃描
        for h in range(height):	#由下向上掃描
            color = im.getpixel((w, h))	#取得圖形指定位置的像素顏色
            if color != (255, 255, 255):
                return w			#返回橢圓邊界最左端的x坐標

def searchRight(width, height, im):
    for w in range(width-1, -1, -1):	#由右向左掃描
        for h in range(height):
            color = im.getpixel((w, h))
            if color != (255, 255, 255):
                return w 			#返回橢圓邊界最右端的x坐標
            
def searchTop(width, height, im):
    for h in range(height-1, -1, -1):
        for w in range(width):
            color = im.getpixel((w,h))
            if color != (255, 255, 255):
                return h			#返回橢圓邊界最上端的y坐標

def searchBottom(width, height, im):
    for h in range(height):
        for w in range(width):
            color = im.getpixel((w,h))
            if color != (255, 255, 255):
                return h			#返回橢圓邊界最下端的y坐標

#巡訪指定資料夾中所有的bmp圖形檔，假設圖形為白色背景，橢圓為其他任意顏色
images = [f for f in os.listdir('testimages') if f.endswith('.bmp')]
for f in images:
    f = 'testimages\\'+f
    im = Image.open(f)
    width, height = im.size		#取得圖形大小
    x0, x1 = searchLeft(width, height, im), searchRight(width, height, im)
    y0, y1 = searchBottom(width, height, im), searchTop(width, height, im)
    center = ((x0+x1)//2, (y0+y1)//2)
    im.putpixel(center, (255,0,0))	#把橢圓中心像素畫成紅色
    im.save(f[0:-4]+'_center.bmp')	#儲存為新圖形檔
im.close()
