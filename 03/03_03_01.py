def check_permission(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username')!='admin':
            raise Exception('Sorry. You are not allowed.')
        return func(*args, **kwargs)
    return wrapper

class ReadWriteFile(object):
    #把函數check_permission作為裝飾器使用
    @check_permission
    def read(self, username, filename):
        return open(filename,'r').read()

    def write(self, username, filename, content):
        open(filename,'a+').write(content)
    #把函數check_permission作為普通函數使用
    write = check_permission(write)

t = ReadWriteFile()
print('Originally.......')
print(t.read(username='admin', filename=r'd:\sample.txt'))
print('Now, try to write to a file........')
t.write(username='admin', filename=r'd:\sample.txt', content='\nhello world')
print('After calling to write...........')
print(t.read(username='admin', filename=r'd:\sample.txt'))
