import turtle

t = turtle.Pen()		#使用鋼筆
t.color(1, 0, 0)		#設定鋼筆顏色
t.up()				#抬起，移動時不畫
t.backward(280)		#後退280像素
t.left(90)			#左轉90度
t.forward(100)			#前進100像素
t.right(90)			#右轉90度
t.down()				#落筆，開始畫
for i in range(4):		#繪製矩形
    t.forward(150)
    t.left(90)

t.color(0, 0, 0)
t.up()
t.forward(200)
t.down()
for i in range(3):		#繪製等邊三角形
    t.forward(200)
    t.left(120)

t.up()
t.forward(100)
t.down()
t.fillcolor(1, 0.6, 0.3)	#設定填充色
t.begin_fill()
t.circle(50)			#繪製有填充色的圓，半徑50像素
t.end_fill()

t.up()
t.forward(120)
t.left(90)
t.forward(90)
t.right(90)
t.down()
t.width(3)			#設定鋼筆粗細
t.fillcolor(0, 0.6, 0.8)	#設定填充色
t.begin_fill()
for i in range(5): 		#繪製五角星
    t.forward(150)
    t.right(144)
t.end_fill()

t.up()
t.backward(270)
t.right(90)
t.forward(150)
t.write('Created using turtle, by董付國', font=('隸書', 16, 'normal'))
t.forward(10)
t.left(90)
t.width(1)
t.down()
t.forward(350)
