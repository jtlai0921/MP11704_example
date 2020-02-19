import os
import stat

def remove_readonly(func, path):		#定義回呼函數
    os.chmod(path, stat.S_IWRITE)		#刪除檔案的唯讀屬性
    func(path)						#再次呼叫剛剛失敗的函數

def del_dir(path, onerror=None):
    for file in os.listdir(path):
        file_or_dir = os.path.join(path,file)
        if os.path.isdir(file_or_dir) and not os.path.islink(file_or_dir):
            del_dir(file_or_dir)		#遞迴刪除子資料夾及其檔案
        else:
            try:
                os.remove(file_or_dir)	#嘗試刪除該檔，
            except:					#刪除失敗
                if onerror and callable(onerror):
                    onerror(os.remove, file_or_dir)	#自動呼叫回呼函數
                else:
                    print('You have an exception but did not capture it.')
    os.rmdir(path)					#刪除資料夾

del_dir("E:\\old", remove_readonly)	#呼叫函數，並指定回呼函數
