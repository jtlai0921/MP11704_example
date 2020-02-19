from PIL import Image

def qipan(fileName, width, height, color1, color2):
    #產生空白圖形
    im = Image.new('RGB',(width,height))
    for h in range(height):
        for w in range(width):
            #填充顏色交叉的圖案
            if (int(h/height*8)+int(w/width*8)) % 2 == 0:
                im.putpixel((w,h), color1)
            else:
                im.putpixel((w,h), color2)
    #儲存圖形檔
    im.save(fileName)

if __name__=='__main__':
    fileName = 'qipan.jpg'
    qipan(fileName, 500, 500, (128,128,128), (10,10,10))
