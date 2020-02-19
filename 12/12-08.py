from PIL import Image
from math import floor

def textureMap(srcTextureFile, dstSurfaceFile, dstWidth, dstHeight):
    '''srcTextureFile:原始圖片
       dstSurfaceFile:模擬目標物體表面
       dstWidth:目標物體表面寬度
       dstHeight:目標物體表面高度
    #開啟原始圖片
    srcTexture = Image.open(srcTextureFile)
    #建立指定尺寸的目標物體表面
    dstSurface = Image.new('RGBA', (dstWidth, dstHeight))
    srcWidth, srcHeight = srcTexture.size
    #根據目標物體表面尺寸，計算並取得原始圖片中對應位置的像素值
    for w in range(dstWidth):
        for h in range(dstHeight):
            x, y = floor(w/dstWidth*srcWidth), floor(h/dstHeight*srcHeight)
            dstSurface.putpixel((w,h), srcTexture.getpixel((x,y)))
    dstSurface.save(dstSurfaceFile)
    dstSurface.close()
    srcTexture.close()
    #也可以嘗試下面的寫法，更簡單一些
    '''
    srcTexture = Image.open(srcTextureFile)
    srcTexture = srcTexture.resize((dstWidth,dstHeight))
    srcTexture.save(dstSurfaceFile)
    srcTexture.close()


#測試
textureMap('sample.jpg', r'new.jpg', 200, 250)
