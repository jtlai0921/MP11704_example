#自訂集合類別
class Set(object):
    def __init__(self, data=None):
        if data==None:
            self.__data = []
        else:
            if not hasattr(data, '__iter__'):
                #提供的資料不可反覆運算，產生實體失敗
                raise Exception('必須提供可反覆運算的資料類型')
            temp = []
            for item in data:
                #集合中的元素必須可雜湊
                #這裡的可雜湊，與第14章介紹的安全雜湊演算法並不一樣
                hash(item)
                if not item in temp:
                    temp.append(item)
            self.__data = temp

    #解構函數
    def __del__(self):
        del self.__data

    #增加元素，要求元素必須可雜湊
    def add(self, value):
        hash(value)
        if value not in self.__data:
            self.__data.append(value)
        else:
            print('元素已存在，操作被忽略')

    #刪除元素
    def remove(self, value):
        if value in self.__data:
            self.__data.remove(value)
            print('刪除成功')
        else:
            print('元素不存在，刪除操作被忽略')

    #隨機彈出並返回一個元素
    def pop(self):
        if not self.__data:
            print('集合已空，彈出操作被忽略')
            return
        import random
        item = random.choice(self.__data)
        print(item)
        self.__data.remove(item)

    #運算子重載，集合差集運算
    def __sub__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        #空集合
        result = Set()
        #如果一個元素屬於目前集合而非另一個集合，則新增
        for item in self.__data:
            if item not in anotherSet.__data:
                result.__data.append(item)
        return result
    
    #提供方法，集合差集運算
    def difference(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        return self - anotherSet

    
    #|運算子重載，集合聯集運算
    def __or__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        result = Set(self.__data)
        for item in anotherSet.__data:
            if item not in result.__data:
                result.__data.append(item)
        return result
    
    #提供方法，集合聯集運算
    def union(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        return self | anotherSet
    
    #&運算子重載，集合交集運算
    def __and__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        result = Set()
        for item in self.__data:
            if item in anotherSet.__data:
                result.__data.append(item)
        return result
        
    #^運算子重載，集合對稱差集
    def __xor__(self, anotherSet):
        return (self-anotherSet) | (anotherSet-self)

    #提供方法，集合對稱差集運算
    def symetric_difference(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        return self ^ anotherSet

    #==運算子重載，判斷兩個集合是否相等
    def __eq__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        if sorted(self.__data) == sorted(anotherSet.__data):
            return True
        else:
            return False

    #>運算子重載，集合包含關係
    def __gt__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        if self != anotherSet:
            flag1 = True
            for item in self.__data:
                if item not in anotherSet.__data:
                    #目前集合中有的元素不屬於另一個集合
                    flag1 = False
                    break
            flag2 = True
            for item in anotherSet.__data:
                if item not in self.__data:
                    #另一個集合中有的元素不屬於目前集合
                    flag2 = False
                    break
            if  not flag1 and flag2:
                return True
            return False

    #>=運算子重載，集合包含關係
    def __ge__(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        return self==anotherSet or self>anotherSet
    
    #提供方法，判斷目前集合是否為另一個集合的真子集
    def issubset(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        if self < anotherSet:
            return True
        else:
            return False

    #提供方法，判斷目前集合是否為另一個集合的超集合
    def issuperset(self, anotherSet):
        if not isinstance(anotherSet, Set):
            raise Exception('類型錯誤')
        if self > anotherSet:
            return True
        else:
            return False


    #提供方法，清空集合所有元素
    def clear(self):
        while self.__data:
            del self.__data[-1]
        print('集合已清空')

    #運算子重載，使得集合可反覆運算
    def __iter__(self):
        return iter(self.__data)

    #運算子重載，支援in運算子
    def __contains__(self, value):
        if value in self.__data:
            return True
        else:
            return False

    #支援內建函數len()
    def __len__(self):
        return len(self.__data)
        
    #直接查看該類別物件時，呼叫此函數
    def __repr__(self):
        return '{'+str(self.__data)[1:-1]+'}'

    #以print()函數輸出該類別物件時，呼叫此函數
    def __str__(self):
        return '{'+str(self.__data)[1:-1]+'}'
