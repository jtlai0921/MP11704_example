class BinaryTree:
    def __init__(self, value):
        self.__left = None
        self.__right =  None
        self.__data = value

    #解構函數
    def __del__(self):
        del self.__data

    def insertLeftChild(self, value):	#建立左子樹
        if self.__left:
            print('__left child tree already exists.')
        else:
            self.__left = BinaryTree(value)
            return self.__left
        
    def insertRightChild(self, value):	#建立右子樹
        if self.__right:
            print('Right child tree already exists.')
        else:
            self.__right = BinaryTree(value)
            return self.__right
        
    def show(self):
        print(self.__data)

    def preOrder(self):			#前序遍歷
        print(self.__data)			#輸出根節點的值
        if self.__left:
            self.__left.preOrder()	#遍歷左子樹
        if self.__right:
            self.__right.preOrder()	#遍歷右子樹

    def postOrder(self):			#後序遍歷
        if self.__left:
            self.__left.postOrder()
        if self.__right:
            self.__right.postOrder()
        print(self.__data)

    def inOrder(self):			#中序遍歷
        if self.__left:
            self.__left.inOrder()
        print(self.__data)
        if self.__right:
            self.__right.inOrder()

if __name__ == '__main__':
    print('Please use me as a module.')
