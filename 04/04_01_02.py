class A:
	def __init__(self, value1 = 0, value2 = 0):	#建構函數
		self._value1 = value1
		self.__value2 = value2			#私有成員
	def setValue(self, value1, value2):	#成員方法
		self._value1 = value1
		self.__value2 = value2	#類別內部可以直接存取私有成員
	def show(self):				#成員方法
		print(self._value1)
		print(self.__value2)
