import socket
import threading
import os
import struct

#�ϥΪ̱b���B�K�X�B�D�ؿ�
#�]�i�H��o�Ǹ�Ʀs����Ʈw
users = {'zhangsan':{'pwd':'zhangsan1234', 'home':r'c:\python 3.5'},
         'lisi':{'pwd':'lisi567', 'home':'c:\\'}}

def server(conn,addr, home):
    print('�s�Τ�ݡG'+str(addr))
    #�i�J�ثe�b���D�ؿ�
    os.chdir(home)
    while True:
        data = conn.recv(100).decode().lower()
        #��ܥΤ�ݿ�J���C�@�D�R�O
        print(data)
        #�Τ�ݰh�X
        if data in ('quit', 'q'):
            break
        #�d�ݥثe��Ƨ����ɮצC��
        elif data in ('list', 'ls', 'dir'):
            files = str(os.listdir(os.getcwd()))
            files = files.encode()
            #���ǰe�줸�զr��j�p�A�A�ǰe�줸�զr��
            conn.send(struct.pack('I', len(files)))
            conn.send(files)
        #�����ܤW�@�h�ؿ�
        elif ''.join(data.split()) == 'cd..':
            cwd = os.getcwd()
            newCwd = cwd[:cwd.rindex('\\')]
            #�Ҽ{�ڥؿ������p
            if newCwd[-1] == ':':
                newCwd += '\\'
            #���w�ϥΪ̥D�ؿ�
            if newCwd.lower().startswith(home):
                os.chdir(newCwd)
                conn.send(b'ok')
            else:
                conn.send(b'error')
        #�d�ݥثe���ؿ�
        elif data in ('cwd', 'cd'):
            conn.send(str(os.getcwd()).encode())
        elif data.startswith('cd '):
            #���w�̤j���j���ơA�Ҽ{�ت���Ƨ��a���Ů檺���p
            #�u���\�H�۹���|�i�����
            data = data.split(maxsplit=1)
            if len(data) == 2 and  os.path.isdir(data[1]) \
               and data[1]!=os.path.abspath(data[1]):
                os.chdir(data[1])
                conn.send(b'ok')
            else:
                conn.send(b'error')
        #�U���ɮ�
        elif data.startswith('get '):
            data = data.split(maxsplit=1)
            #�ˬd�ɮ׬O�_�s�b
            if len(data) == 2 and os.path.isfile(data[1]):
                conn.send(b'ok')
                fp = open(data[1], 'rb')
                while True:
                    content = fp.read(4096)
                    #�ǰe�ɮ׵���
                    if not content:
                        conn.send(b'overxxxx')
                        break
                    #�ǰe�ɮפ��e
                    conn.send(content)
                    if conn.recv(10) == b'ok':
                        continue
                fp.close()
            else:
                conn.send(b'no')
        #�L�ĩR�O
        else:
            pass
            
    conn.close()
    print(str(addr)+'�����s��')

#�إ�Socket�A��ť���a�s����A�õ��ݥΤ�ݳs��
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 10600))
sock.listen(5)
while True:
    conn, addr = sock.accept()
    #���ҥΤ�ݿ�J���b���M�K�X�O�_���T
    userId, userPwd = conn.recv(1024).decode().split(',')
    if userId in users and users[userId]['pwd'] == userPwd:
        conn.send(b'ok')
        #���C�ӥΤ�ݳs���إ߻P�Ұʤ@�Ӱ����
        #�ѼƬ��s���B�Τ�ݦ�}�B�b���D�ؿ�
        home = users[userId]['home']
        t = threading.Thread(target=server, args=(conn,addr,home))
        t.daemon = True
        t.start()
    else:
        conn.send(b'error')
