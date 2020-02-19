class simNumpyArray(object):
    def __init__(self, p):
        '''可接收列表、元組、range物件等類型的資料，並且每個元素都必須為數字'''
        if type(p) not in (list, tuple, range):
            print('data type error')
            return
        for item in p:
            #下面這行用來判斷參數類型，可以改成這樣
            #if isinstance(item, (int, float, complex)):
            if type(item) not in (int, float, complex):
                print('data type error')
                return
        self.__data = [list(p)]
        self.__row = 1
        self.__col = len(p)

    #解構函數
    def __del__(self):
        del self.__data

    #修改大小，首先檢查給定的大小參數是否合適
    def reshape(self, size):
        '''參數必須是元組或列表，如(row,col)或[row,col]
           row或col其中一個可以為-1，表示自動計算
        '''
        if not (isinstance(size, list) or isinstance(size, tuple)):
            print('size parameter error')
            return
        if len(size) != 2:
            print('size parameter error')
            return
        if (not isinstance(size[0],int)) or (not isinstance(size[1],int)):
            print('size parameter error')
            return
        if size[0] != -1 and size[1] != -1 and size[0]*size[1] != self.__row*self.__col:
            print('size parameter error')
            return
        #行數或列數為-1，表示該值自動計算
        if size[0] == -1:
            if size[1] == -1 or (self.__row*self.__col)%size[1] != 0:
                print('size parameter error')
                return
        if size[1] == -1:
            if size[0] == -1 or (self.__row*self.__col)%size[0] != 0:
                print('size parameter error')
                return
                
        #重新合併資料
        data = [t for i in self.__data for t in i]
        #修改大小
        if size[0] == -1:
            self.__row = int(self.__row*self.__col/size[1])
            self.__col = size[1]
        elif size[1] == -1:
            self.__col = int(self.__row*self.__col/size[0])
            self.__row = size[0]
        else:
            self.__row = size[0]
            self.__col = size[1]            
        self.__data = [[data[row*self.__col+col] for col in range(self.__col)] for row in range(self.__row)]

    #在交互模式下直接使用變數名稱作為運算式，查看值時呼叫該函數
    def __repr__(self):
        #return repr('\n'.join(map(str, self.__data)))
        for i in self.__data:
            print(i)
        return ''

    #以print()函數輸出值時呼叫該函數
    def __str__(self):
        return '\n'.join(map(str, self.__data))
    
    #屬性，矩陣轉置
    @property
    def T(self):
        b = simNumpyArray([t for i in self.__data for t in i])
        b.reshape((self.__row, self.__col))
        b.__data = list(map(list,zip(*b.__data)))
        b.__row, b.__col = b.__col, b.__row
        return b

    #通用程式碼，適用於矩陣與整數、實數、複數的加、減、乘、除、整除、指數
    def __operate(self, n, op):
        b = simNumpyArray([t for i in self.__data for t in i])
        b.reshape((self.__row, self.__col))
        b.__data = [[eval(str(j)+op+str(n)) for j in item] for item in b.__data]
        return b

    #通用程式碼，適用於矩陣之間的加、減
    def __matrixAddSub(self, n, op):
        c = simNumpyArray([1])
        c.__row = self.__row
        c.__col = self.__col
        c.__data = [[eval(str(x[i])+op+str(y[i])) for i in range(len(x))] for x,y in zip(self.__data, n.__data)]
        return c
    
    #所有元素統一加一個數字，或者兩個矩陣相加
    def __add__(self, n):
        #若參數是整數或實數，則返回矩陣
        #其中每個元素為原矩陣中元素與該整數或實數相加的結果
        if type(n) in (int, float, complex):
            return self.__operate(n, '+')
        elif isinstance(n, simNumpyArray):
            #如果參數為同類型矩陣，且大小一致，則為兩個矩陣的對應元素相加
            if n.__row==self.__row and n.__col==self.__col:
                return self.__matrixAddSub(n, '+')
            else:
                print('two matrix must be the same size')
                return
        else:
            print('data type error')
            return
            
    #所有元素統一減一個數字，或者兩個矩陣相減
    def __sub__(self, n):
        #若參數是整數或實數，則返回矩陣
        #其中每個元素為原矩陣中元素與該整數或實數相減的結果
        if type(n) in (int, float, complex):
            return self.__operate(n, '-')
        elif isinstance(n, simNumpyArray):
            #如果參數為同類型矩陣，且大小一致，則為兩個矩陣的對應元素相減
            if n.__row==self.__row and n.__col==self.__col:
                #先產生一個實體的臨時物件，內容為[1]
                return self.__matrixAddSub(n, '-')
            else:
                print('two matrix must be the same size')
                return
        else:
            print('data type error')
            return
            
    #所有元素統一乘一個數字，或者兩個矩陣相乘
    def __mul__(self, n):
        #若參數是整數或實數，則返回矩陣
        #其中每個元素為原矩陣中元素與該整數或實數相乘的結果
        if type(n) in (int, float, complex):
            return self.__operate(n, '*')
        elif isinstance(n, simNumpyArray):
            #如果參數為同類型矩陣，且第一個矩陣的列數等於第二個矩陣的行數
            if n.__row==self.__col:     
                data = []
                for row in self.__data:
                    t = []
                    for ii in range(n.__col):
                        col = [c[ii] for c in n.__data]
                        tt = sum([i*j for i,j in zip(row,col)])
                        t.append(tt)
                    data.append(t)
                c = simNumpyArray([t for i in data for t in i])
                c.reshape((self.__row, n.__col))
                return c
            else:
                print('size error.')
                return
        else:
            print('data type error')
            return
        
    #所有元素統一除以一個數字，此處採用Python 3.x編寫，真除法
    def __truediv__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '/')
        else:
            print('data type error')
            return

    #矩陣元素與數字計算整商
    def __floordiv__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '//')
        else:
            print('data type error')
            return
        
    #矩陣與數字的指數運算
    def __pow__(self, n):
        if type(n) in (int, float, complex):
            return self.__operate(n, '**')
        else:
            print('data type error')
            return

    #測試兩個矩陣是否相等
    def __eq__(self, n):
        if isinstance(n, simNumpyArray):
            if self.__data == n.__data:
                return True
            else:
                return False
        else:
            print('data type error')
            return

    #測試矩陣本身是否小於另一個矩陣
    def __lt__(self, n):
        if isinstance(n, simNumpyArray):
            if self.__data < n.__data:
                return True
            else:
                return False
        else:
            print('data type error')
            return

    #成員測試運算子
    def __contains__(self, v):
        if v in self.__data:
            return True
        else:
            return False

    #支援反覆運算
    def __iter__(self):
        return iter(self.__data)

    #通用方法，計算三角函數
    def __triangle(self, method):
        try:
            b = simNumpyArray([t for i in self.__data for t in i])
            b.reshape((self.__row, self.__col))
            b.__data = [[eval("__import__('math')."+method+"("+str(j)+")") for j in item] for item in b.__data]
            return b
        except:
            return 'method error'
        
    #屬性，對所有元素求正弦
    @property
    def Sin(self):        
        return self.__triangle('sin')

    #屬性，對所有元素求餘弦
    @property
    def Cos(self):
        return self.__triangle('cos')
