#要測試的模組，在本書第4章
import Stack
#Python單元測試標準庫
import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        #測試之前以附加模式開啟指定檔案
        self.fp = open('D:\\test_Stack_result.txt', 'a+')

    def tearDown(self):
        #測試結束後關閉檔案
        self.fp.close()
        
    def test_isEmpty(self):
        try:
            s = Stack.Stack()
            #確保函數返回結果為True
            self.assertTrue(s.isEmpty())
            self.fp.write('isEmpty passed\n')
        except Exception as e:
            self.fp.write('isEmpty failed\n')

    def test_empty(self):
        try:
            s = Stack.Stack(5)
            for i in ['a', 'b', 'c']:
                s.push(i)
            #測試清空堆疊操作是否正常
            s.empty()
            self.assertTrue(s.isEmpty())
            self.fp.write('empty passed\n')
        except Exception as e:
            self.fp.write('empty failed\n')

    def test_isFull(self):
        try:
            s = Stack.Stack(3)
            s.push(1)
            s.push(2)
            s.push(3)
            self.assertTrue(s.isFull())
            self.fp.write('isFull passed\n')
        except Exception as e:
            self.fp.write('isFull failed\n')

    def test_pushpop(self):
        try:
            s = Stack.Stack()
            s.push(3)
            #確保推入堆疊後立刻彈出，以得到原來的元素
            self.assertEqual(s.pop(), 3)
            s.push('a')
            self.assertEqual(s.pop(), 'a')
            self.fp.write('push and pop passed\n')
        except Exception as e:
            self.fp.write('push or pop failed\n')

    def test_setSize(self):
        try:
            s = Stack.Stack(8)
            for i in range(8):
                s.push(i)
            self.assertTrue(s.isFull())
            #測試擴大堆疊空間是否正常
            s.setSize(9)
            s.push(8)
            self.assertTrue(s.isFull())
            self.assertEqual(s.pop(), 8)
            #測試縮小堆疊空間是否正常
            s.setSize(4)
            self.assertTrue(s.isFull())
            self.assertEqual(s.pop(), 3)
            self.fp.write('setSize passed\n')
        except Exception as e:
            self.fp.write('setSize failed\n')
        
if __name__ == '__main__':
    unittest.main()
