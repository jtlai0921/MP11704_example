import random
import string
import codecs

#常用中文字Unicode編碼表（部分），完整清單詳見配套原始程式碼
StringBase = '\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba'
#轉換為中文
StringBase = ''.join(StringBase.split('\\u')) 
                     
def getEmail():
    #常見功能變數名稱尾碼，可以隨意擴展該列表
    suffix = ['.com', '.org', '.net', '.cn']
    characters = string.ascii_letters+string.digits+'_'
    username = ''.join((random.choice(characters) for i in range(random.randint(6,12))))
    domain = ''.join((random.choice(characters) for i in range(random.randint(3,6))))
    return username+'@'+domain+random.choice(suffix)

def getTelNo():
    return ''.join((str(random.randint(0,9)) for i in range(11)))

def getNameOrAddress(flag):
    '''flag=1表示返回隨機姓名，flag=0表示返回隨機地址'''
    result = ''
    if flag==1:
        #大部分中國人姓名在2-4個中文字
        rangestart, rangeend = 2, 5
    elif flag==0:
        #假設位址在10-30個中文字之間
        rangestart, rangeend = 10, 31
    else:
        print('flag must be 1 or 0')
        return ''
    for i in range(rangestart, rangeend):
        result += random.choice(StringBase)
    return result

def getSex():
    return random.choice(('男', '女'))

def getAge():
    return str(random.randint(18,100))

def main(filename):
    with codecs.open(filename, 'w', 'utf-8') as fp:
        fp.write('Name,Sex,Age,TelNO,Address,Email\n')
        #隨機產生200個人的資訊
        for i in range(200):
            name = getNameOrAddress(1)
            sex = getSex()
            age = getAge()
            tel = getTelNo()
            address = getNameOrAddress(0)
            email = getEmail()
            line = ','.join([name, sex, age, tel, address, email]) + '\n'
            fp.write(line)
            
def output(filename):
    with codecs.open(filename, 'r', 'utf-8') as fp:
        while True:
            line = fp.readline()
            if not line:
                return
            line = line.split(',')
            for i in line:
                print(i, end=',')
            print()
            
if __name__=='__main__':
    filename = 'information.txt'
    main(filename)
    output(filename)
