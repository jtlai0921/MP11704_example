import socket
import sys
import re
import struct
import getpass

def main(serverIP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverIP, 10600))
    userId = input('�п�J�b���W�١G')
    #�Hgetpass�Ҳժ�getpass()��k���o�K�X�A�����
    userPwd = getpass.getpass('�п�J�K�X�G')
    message = userId+','+userPwd
    sock.send(message.encode())
    login = sock.recv(100)
    #���ҬO�_�n�����\
    if login == b'error':
        print('�b���W�٩αK�X���~')
        return
    #��ƽs�X�j�p
    intSize = struct.calcsize('I')
    while True:
        #�����Τ�ݩR�O�A�䤤##>�O���ܲŸ�
        command = input('##> ').lower().strip()
        #����J���󦳮Ħr���A���e�i�J�U�@���j��A���ݨϥΪ��~���J
        if not command:
            continue
        #�V���A�ݶǰe�R�O
        command = ' '.join(command.split())
        sock.send(command.encode())
        #�h�X
        if command in ('quit', 'q'):
            break
        #�d���ɮצC��
        elif command in ('list', 'ls', 'dir'):
            #�������줸�զr��j�p�A�A�ھڱ��p�����A��ƶq���줸�զr��
            loc_size = struct.unpack('I', sock.recv(intSize))[0]
            files = eval(sock.recv(loc_size).decode())
            for item in files:
                print(item)
        #�����ܤW�@�h�ؿ�
        elif ''.join(command.split()) == 'cd..':
            print(sock.recv(100).decode())
        #�d�ݥثe�u�@�ؿ�
        elif command in ('cwd', 'cd'):
            print(sock.recv(1024).decode())
        #�����ܤl��Ƨ�
        elif command.startswith('cd '):
            print(sock.recv(100).decode())
        #�q���A���U���ɮ�
        elif command.startswith('get '):
            isFileExist = sock.recv(20)
            #�ɮפ��s�b
            if isFileExist != b'ok':
                print('error')
            #�ɮצs�b�A�}�l�U��
            else:
                print('downloading.', end='')
                fp = open(command.split()[1], 'wb')
                while True:
                    #��ܶi��
                    print('.', end='')
                    data = sock.recv(4096)
                    if data == b'overxxxx':
                        break
                    fp.write(data)
                    sock.send(b'ok')
                fp.close()
                print('ok')
                
        #�L�ĩR�O
        else:
            print('�L�ĩR�O')
    sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:{0} serverIPAddress'.format(sys.argv[0]))
        exit()
    serverIP = sys.argv[1]
    #�H�W�h�B�⦡�P�_���A����}�O�_���X�k��IP��}
    if re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', serverIP):
        main(serverIP)
    else:
        print('���A����}���X�k')
        exit()
