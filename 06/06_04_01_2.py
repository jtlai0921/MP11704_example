import os

def visitDir2(path):
    if not os.path.isdir(path):
        print('Error:"', path, '" is not a directory or does not exist.')
        return
    list_dirs = os.walk(path) 
    for root, dirs, files in list_dirs:		#遍歷該元組的目錄和檔案資訊
        for d in dirs: 
            print(os.path.join(root, d))		#獲取得完整路徑
        for f in files: 
            print(os.path.join(root, f))		#獲取得檔案絕對路徑
