import os
import sys
import zipfile				#zipfile是標準庫
try:
    from unrar import rarfile	#嘗試匯入擴展庫，如果沒有就臨時安裝
except:
    path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install --upgrade pip'
    os.system(path)
    path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install unrar'
    os.system(path)
    from unrar import rarfile    

def decryptRarZipFile(filename):
    if filename.endswith('.zip'):
        fp = zipfile.ZipFile(filename)
    elif filename.endswith('.rar'):
        fp = rarfile.RarFile(filename)
    desPath = filename[:-4]	#解壓縮的目的資料夾
    if not os.path.exists(desPath):
        os.mkdir(desPath)
    try:					#嘗試不用密碼解壓縮
        fp.extractall(desPath)
        fp.close()
        print('No password')
        return
    except: 				#使用密碼字典進行暴力破解
        try:
            fpPwd = open('pwddict.txt')
        except:
            print('No dict file pwddict.txt in current directory.')
            return
        for pwd in fpPwd:
            pwd = pwd.rstrip()
            try:
                if filename.endswith('.zip'):
                    for file in fp.namelist():	#重新編碼再解碼，避免中文亂碼
                        fp.extract(file, path=desPath, pwd=pwd.encode())
                        os.rename(desPath+'\\'+file,
                                  desPath+'\\'+file.encode('cp437').decode('gbk'))
                    print('Success! ====>'+pwd)
                    fp.close()
                    break
                elif filename.endswith('.rar'):
                    fp.extractall(path=desPath, pwd=pwd)
                    print('Success! ====>'+pwd)
                    fp.close()
                    break
            except:
                pass
        fpPwd.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    if os.path.isfile(filename) and filename.endswith(('.zip', '.rar')):
        decryptRarZipFile(filename)
    else:
        print('Must be Rar or Zip file')
