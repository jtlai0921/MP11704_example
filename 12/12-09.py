from random import randint
from PIL import Image

#根據原始24位元BMP影像檔，產生指定數量含有隨機噪點的臨時圖形
def addNoise(fileName, num):
    if not fileName.endswith('.bmp'):
        print('Must be bmp image')
        return
    for i in range(num):
        im = Image.open(fileName)
        width, height = im.size
        n = randint(1, 20)
        for j in range(n):
            w = randint(0, width-1)
            h = randint(0, height-1)
            im.putpixel((w,h), (0,0,0))
        im.save(fileName[:-4]+'_'+str(i+1)+'.bmp')

#根據多個含有隨機噪點的圖形，對應位置像素計算平均值，以產生結果圖形
def mergeOne(fileName, num):
    if not fileName.endswith('.bmp'):
        print('Must be bmp image')
        return
    ims = [Image.open(fileName[:-4]+'_'+str(i+1)+'.bmp') for i in range(num)]
    im = Image.new('RGB', ims[0].size, (255,255,255))
    for w in range(im.size[0]):
        for h in range(im.size[1]):
            r, g, b = [0]*3
            for tempIm in ims:
                value = tempIm.getpixel((w,h))
                r += value[0]
                g += value[1]
                b += value[2]
            r = r//num
            g = g//num
            b = b//num
            im.putpixel((w,h), (r,g,b))
    im.save(fileName[:-4]+'_result.bmp')

#對比合併後的圖形和原始圖形之間的相似度
def compare(fileName):
    im1 = Image.open(fileName)
    im2 = Image.open(fileName[:-4]+'_result.bmp')
    width, height = im1.size
    total = width * height
    right = 0
    expectedRatio = 0.05
    for w in range(width):
        for h in range(height):
            r1, g1, b1 = im1.getpixel((w,h))
            r2, g2, b2 = im2.getpixel((w,h))
            if (abs(r1-r2),abs(g1-g2),abs(b1-b2)) < (255*expectedRatio,)*3:
                right += 1
    return (total, right)

if __name__ == '__main__':
    #產生32個臨時圖形後進行融合，並對比融合後的圖形與原始圖形的相似度
    addNoise('test.bmp', 32)
    mergeOne('test.bmp', 32)
    result = compare('test.bmp')
    print('Total number of pixels:{0[0]},right number:{0[1]}'.format(result))
