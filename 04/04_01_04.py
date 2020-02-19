class Root:
	__total = 0
	def __init__(self, v):	#建構函數
			self.__value = v
			Root.__total += 1

	def show(self):		#普通的實例方法
			print('self.__value:', self.__value)
			print('Root.__total:', Root.__total)

	@classmethod			#修飾器，宣告類別方法
	def classShowTotal(cls):	#類別方法
			print(cls.__total)

	@staticmethod			#修飾器，宣告靜態方法
	def staticShowTotal():	#靜態方法
			print(Root.__total)
