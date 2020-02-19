import sys
from math import pi as PI
from math import sin, cos
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
##下載64 bit PyOpenGL安装包
##http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl
##pip install file_name.whl
class MyPyOpenGLTest:
    #重寫建構函數，初始化OpenGL環境，指定顯示模式以及用來繪圖的函數
    def __init__(self, width = 640, height = 480, title = 'MyPyOpenGLTest'.encode('big5')):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window = glutCreateWindow(title)
        #指定繪製函數
        glutDisplayFunc(self.Draw)
        glutIdleFunc(self.Draw)
        self.InitGL(width, height)

    #根據特定的需求，進一步完成OpenGL的初始化
    def InitGL(self, width, height):
        #初始化視窗背景為白色
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        #光滑渲染
        glEnable(GL_BLEND)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)        
        glMatrixMode(GL_PROJECTION)
        #反走樣，也稱抗鋸齒
        glHint(GL_POINT_SMOOTH_HINT,GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT,GL_FASTEST)
        glLoadIdentity()
        #透視投影變換
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    #定義自己的繪圖函數
    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        #平移
        glTranslatef(-3.0, 2.0, -8.0)
        #繪製二維圖形，z座標為0
        #指定模式，繪製多邊形
        glBegin(GL_POLYGON)
        #設定頂點顏色
        glColor3f(1.0, 0.0, 0.0)
        #繪製多邊形頂點
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, -1.0, 0.0)
        #結束本次繪製
        glEnd()
        
        glTranslatef(3, -1, 0.0)
        
        #繪製三維圖形，三維線條
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 3.0)
        glEnd()

        glTranslatef(-0.3, 1, 0)

        #使用折線繪製圓
        glBegin(GL_LINE_LOOP)
        n = 100
        theta = 2*PI/n
        r = 0.8
        for i in range(100):
            x = r*cos(i*theta)
            y = r*sin(i*theta)
            glVertex3f(x, y, 0)
        glEnd()
        
        glutSwapBuffers()

    #訊息主迴圈
    def MainLoop(self):
        glutMainLoop()

if __name__ == '__main__':
    #產生實體視窗物件，執行程式，啟動訊息主迴圈
    w = MyPyOpenGLTest()
    w.MainLoop()
