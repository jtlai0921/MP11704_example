def getBezier(self, P0, P1, P2, P3, t):
    a0 = (1-t)**3
    a1 = 3 * (1-t)**2 * t
    a2 = 3 * t**2 * (1-t)
    a3 = t**3

    x = a0*P0[0] + a1*P1[0] + a2*P2[0] + a3*P3[0]
    y = a0*P0[1] + a1*P1[1] + a2*P2[1] + a3*P3[1]
    z = a0*P0[2] + a1*P1[2] + a2*P2[2] + a3*P3[2]

    return (x, y, z)

def Draw(self):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #平移
    glTranslatef(-3.0, 0.0, -8.0)
    #指定三次貝茲曲線的四個控制點座標
    P0 = (-4, -2, -9)
    P1 = (-0.5, 3, 0)
    P2 = (2, -3, 0)
    P3 = (4.5, 2, 0)
    #指定模式，繪製連續的折線
    glBegin(GL_LINE_STRIP)
    #設定頂點顏色
    glColor3f(0.0, 0.0, 0.0)
    #使用100段直線條的拼接，以便逼近三次貝茲曲線
    for i in range(101):
        #參數t必須是介於[0,1]之間的實數
        t = i/100.0
        p = self.getBezier(P0, P1, P2, P3, t)
        glVertex3f(*p)
        
    #結束本次繪製
    glEnd()       
        
    glutSwapBuffers()
