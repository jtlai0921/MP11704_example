class Car(object):
    price = 100000				#屬於類別的資料成員
    def __init__(self, c):
        self.color = c			#屬於物件的資料成員

car1 = Car("Red")				#產生實體物件
car2 = Car("Blue")
print(car1.color, Car.price)	#存取物件和類別的資料成員
Car.price = 110000				#修改類別屬性
Car.name = 'QQ'					#動態增加類別屬性
car1.color = "Yellow"			#修改實例屬性
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)
def setSpeed(self, s):
    self.speed = s
car1.setSpeed = types.MethodType(setSpeed, car1)	#動態為物件增加成員方法
car1.setSpeed(50)				#呼叫物件的成員方法
print(car1.speed)
