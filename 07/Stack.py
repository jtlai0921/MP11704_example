class Stack:
    def __init__(self, size = 10):
        self._content = []		#使用列表存放堆疊元素
        self._size = size		#初始堆疊大小
        self._current = 0		#堆疊元素的個數初始化為0

    #解構函數
    def __del__(self):
        del self._content

    def empty(self):
        self._content = []
        self._current = 0
        
    def isEmpty(self):
        return not self._content

    def setSize(self, size):
        #如果縮小堆疊空間，則刪除指定大小之後的既有元素
        if size < self._current:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size
    
    def isFull(self):
        return self._current == self._size
        
    def push(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1	#堆疊的元素個數加1
        else:
            print('Stack Full!')
            
    def pop(self):
        if self._content:
            self._current = self._current - 1	#堆疊的元素個數減1
            return self._content.pop()
        else:
            print('Stack is empty!')
            
    def show(self):
        print(self._content)

    def showRemainderSpace(self):
        print('Stack can still PUSH ', self._size-self._current, ' elements.')

if __name__ == '__main__':
    print('Please use me as a module.')
