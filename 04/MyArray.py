class MyArray:
    '''All the elements in this array must be numbers'''
    def __IsNumber(self, n):
        if not isinstance(n, (int, float, complex)):
            return False
        return True

    #建構函數，進行必要的初始化
    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print('All elements must be numbers')
                    return
            self.__value = list(args)

    #解構函數，釋放內部封裝的列表
    def __del__(self):
        del self.__value

    #重載運算子+
    #陣列的每個元素都與數字n相加，或兩個陣列相加，返回新陣列
    def __add__(self, n):
        if self.__IsNumber(n):
            #陣列的所有元素都與數字n相加
            b = MyArray()
            b.__value = [item+n for item in self.__value]
            return b
        elif isinstance(n, MyArray):
            #兩個等長的陣列對應元素相加
            if len(n.__value)==len(self.__value):
                c = MyArray()
                c.__value = [i+j for i, j in zip(self.__value, n.__value)]
                #for i, j in zip(self.__value, n.__value):
                #    c.__value.append(i+j)
                return c
            else:
                print('Lenght not equal')                
        else:
            print('Not supported')

    #重載運算子-
    ##陣列的每個元素都與數字n相減，返回新陣列
    def __sub__(self, n):
        if not self.__IsNumber(n):
            print('- operating with ', type(n), ' and number type is not supported.')
            return
        b = MyArray()
        b.__value = [item-n for item in self.__value]
        return b

    #重載運算子*
    #陣列的每個元素都與數字n相乘，返回新陣列
    def __mul__(self, n):
        if not self.__IsNumber(n):
            print('* operating with ', type(n), ' and number type is not supported.')
            return
        b = MyArray()
        b.__value = [item*n for item in self.__value]
        return b

    #重載運算子/
    #陣列的每個元素都與數字n相除，返回新陣列
    def __truediv__(self, n):
        if not self.__IsNumber(n):
            print(r'/ operating with ', type(n), ' and number type is not supported.')
            return
        b = MyArray()
        b.__value = [item/n for item in self.__value]
        return b

    #重載運算子//
    #陣列的每個元素都與數字n整除，返回新陣列
    def __floordiv__(self, n):
        if not isinstance(n, int):
            print(n, ' is not an integer')
            return
        b = MyArray()
        b.__value = [item//n for item in self.__value]
        return b

    #重載運算子%
    #陣列的每個元素都與數字n求餘數，返回新陣列
    def __mod__(self, n):
        if not self.__IsNumber(n):
            print(r'% operating with ', type(n), ' and number type is not supported.')
            return
        b = MyArray()
        b.__value = [item%n for item in self.__value]
        return b

    #重載運算子**
    #陣列的每個元素都與數字n進行指數計算，返回新陣列
    def __pow__(self, n):
        if not self.__IsNumber(n):
            print('** operating with ', type(n), ' and number type is not supported.')
            return
        b = MyArray()
        b.__value = [item**n for item in self.__value]
        return b

    def __len__(self):        
        return len(self.__value)

    #直接使用該類別物件作為運算式，藉以查看物件的值
    def __repr__(self):
        #equivalent to return `self.__value`
        return repr(self.__value)

    #支援print()函數查看物件的值
    def __str__(self):
        return str(self.__value)

    #增加元素
    def append(self, v):
        if not self.__IsNumber(v):
            print('Only number can be appended.')
            return
        self.__value.append(v)

    #取得指定下標的元素值，支援以列表或元組指定多個下標
    def __getitem__(self, index): 
        length = len(self.__value)
        #如果指定單個整數作為下標，則直接返回元素值
        if isinstance(index, int) and 0<=index<length: 
            return self.__value[index]
        #以列表或元組指定多個整數下標
        elif isinstance(index, (list,tuple)):
            for i in index:
                if not (isinstance(i,int) and 0<=i<length):
                    return 'index error'
            result = []
            for item in index:
                result.append(self.__value[item])
            return result
        else:
            return 'index error'

    #修改元素值，支援以列表或元組指定多個下標，同時修改多個元素值
    def __setitem__(self, index, value):
        length = len(self.__value)
        #如果下標合法，則直接修改元素值
        if isinstance(index, int) and 0<=index<length:
            self.__value[index] = value
        #支援以列表或元組指定多個下標
        elif isinstance(index, (list,tuple)):
            for i in index:
                if not (isinstance(i,int) and 0<=i<length):
                    raise Exception('index error')
            #如果下標和值都是列表或元組，並且個數一樣
            #則分別為多個下標的元素修改值
            if isinstance(value, (list,tuple)):
                if len(index) == len(value):
                    for i, v in enumerate(index):
                        self.__value[v] = value[i]
                else:
                    raise Exception('values and index must be of the same length')
            #如果指定多個下標和一個普通值，則把多個元素修改為相同的值
            elif isinstance(value, (int,float,complex)):
                for i in index:
                    self.__value[i] = value
            else:
                raise Exception('value error')
        else:
            raise Exception('index error')

    #支援成員測試運算子in，測試陣列是否包含某個元素
    def __contains__(self, v):        
        if v in self.__value:
            return True
        return False

    #模擬向量內積
    def dot(self, v):
        if not isinstance(v, MyArray):
            print(v, ' must be an instance of MyArray.')
            return
        if len(v) != len(self.__value):
            print('The size must be equal.')
            return
        return sum([i*j for i,j in zip(self.__value, v.__value)])
        #b = MyArray()
        #for m, n in zip(v.__value, self.__value):
        #    b.__value.append(m * n)
        #return sum(b.__value)

    #重載運算子==，測試兩個陣列是否相等
    def __eq__(self, v):
        if not isinstance(v, MyArray):
            print(v, ' must be an instance of MyArray.')
            return False
        if self.__value == v.__value:
            return True
        return False

    #重載運算子<，比較兩個陣列大小
    def __lt__(self, v):
        if not isinstance(v, MyArray):
            print(v, ' must be an instance of MyArray.')
            return False
        if self.__value < v.__value:
            return True
        return False

if __name__ == '__main__':
    print('Please use me as a module.')
