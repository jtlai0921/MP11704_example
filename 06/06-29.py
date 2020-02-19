from zipfile import ZipFile
from os import listdir
from os.path import isfile, isdir, join

def addFileIntoZipfile(srcDir, fp):
    for subpath in listdir(srcDir):
        subpath = join(srcDir, subpath)
        if isfile(subpath):
            fp.write(subpath)				#寫入檔案
        elif isdir(subpath):
            fp.write(subpath)				#寫入資料夾
            addFileIntoZipfile(subpath, fp)	#遞迴呼叫

def zipCompress(srcDir, desZipfile):
    fp = ZipFile(desZipfile, mode='a')		#以附加模式開啟或建立zip檔
    addFileIntoZipfile(srcDir, fp)
    fp.close()

paths = [r'd:\temp\python']
for path in paths:
    zipCompress(path, 'test.zip')
