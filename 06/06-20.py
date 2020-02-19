import os
import filecmp
import shutil
import sys

def autoBackup(scrDir, dstDir):
    if ((not os.path.isdir(scrDir)) or (not os.path.isdir(dstDir)) or
      (os.path.abspath(scrDir)!=scrDir) or (os.path.abspath(dstDir)!=dstDir)):
        usage()
    for item in os.listdir(scrDir):
        scrItem = os.path.join(scrDir, item)
        dstItem = scrItem.replace(scrDir,dstDir)
        if os.path.isdir(scrItem):
            #建立新增的資料夾，保證目的資料夾的結構與原始資料夾一致
            if not os.path.exists(dstItem):
                os.makedirs(dstItem)
                print('make directory'+dstItem)
            #遞迴呼叫本身函數
            autoBackup(scrItem, dstItem)
        elif os.path.isfile(scrItem):
            #只複製新增或修改過的檔案
            if ((not os.path.exists(dstItem)) or
               (not filecmp.cmp(scrItem, dstItem, shallow=False))):
                shutil.copyfile(scrItem, dstItem)
                print('file:'+scrItem+'==>'+dstItem)

def usage():
    print('scrDir and dstDir must be existing absolute path of certain directory')
    print('For example:{0} c:\\olddir c:\\newdir'.format(sys.argv[0]))
    sys.exit(0)
    
if __name__=='__main__':
    if len(sys.argv)!=3:
        usage()
    scrDir, dstDir= sys.argv[1], sys.argv[2]
    autoBackup(scrDir, dstDir)
