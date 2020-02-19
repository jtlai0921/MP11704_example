import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MyPyOpenGLTest:
    #重寫建構函數，初始化OpenGL環境，指定顯示模式以及用來繪圖的函數
    def __init__(self, width = 640, height = 480, title = b'Normal_Light'):
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
        #設定燈光與材質屬性
        mat_sp = (1.0, 1.0, 1.0, 1.0)
        mat_sh = [50.0]
        light_position = (-0.5, 1.5, 1, 0)
        yellow_l = (1, 1, 0, 1)
        ambient = (0.1, 0.8, 0.2, 1.0)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_sp)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_sh)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, yellow_l)
        glLightfv(GL_LIGHT0, GL_SPECULAR, yellow_l)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
        #啟用光照模型
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
        #光滑渲染
        glEnable(GL_BLEND)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)        
        glMatrixMode(GL_PROJECTION)
        #反走樣，也稱反鋸齒
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
        glTranslatef(-1.5, 2.0, -8.0)                
        #繪製三維圖形，三維線條
        glBegin(GL_LINES)
        #設定頂點顏色
        glColor3f(1.0, 0.0, 0.0)
        #設定頂點法線
        glNormal3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glColor3f(0.0, 1.0, 0.0)
        glNormal3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 3.0)
        glEnd()

        #球
        glColor3f(0.8, 0.3, 1.0)
        glTranslatef(0, -1.5, 0)
        #第一個參數是球的半徑，後面兩個參數是分段數
        glutSolidSphere(1.0,40,40)
        
        glutSwapBuffers()

    #訊息主迴圈
    def MainLoop(self):
        glutMainLoop()

if __name__ == '__main__':
    #產生實體視窗物件，執行程式，啟動訊息主迴圈
    w = MyPyOpenGLTest()
    w.MainLoop()
