class Test:
	def __init__(self, value):
		self.__value = value

	def __get(self):
		return self.__value

	def __set(self, v):
		self.__value = v

	def __del(self):		#刪除物件的私有資料成員
		del self.__value

	value = property(__get, __set, __del)	#可讀、可寫、可刪除的屬性

	def show(self):
		print(self.__value)
