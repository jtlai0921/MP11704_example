import os 

def visitDir(path): 
    if not os.path.isdir(path):
        print('Error:"', path, '" is not a directory or does not exist.')
        return
    for lists in os.listdir(path): 
        sub_path = os.path.join(path, lists) 
        print(sub_path)
        if os.path.isdir(sub_path):  
            visitDir(sub_path)			#遞迴呼叫
