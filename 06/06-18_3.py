from ctypes import *
from ctypes import wintypes
from time import sleep

#呼叫Windows系統動態連結程式庫user32.dll
user32 = windll.user32
p = wintypes.POINT()
buffer = create_string_buffer(255)

while True:
    sleep(0.5)
    #取得滑鼠位置
    user32.GetCursorPos(byref(p))
    #取得滑鼠所在位置的視窗控制碼
    HWnd = user32.WindowFromPoint(p)
    #註解的程式碼本來可以實現星號密碼查看，在Win7以後的系統失效了
    #dwStyle = user32.GetWindowLongA(HWnd, -16) #-16是GWL_STYLE訊息的值
    #user32.SetWindowWord(HWnd, -16, 0)
    sleep(0.2)
    #取得視窗文字
    user32.SendMessageA(HWnd, 13, 255, byref(buffer)) #13是WM_GETTEXT訊息的值
    #user32.SetWindowLongA(HWnd, -16, dwStyle)
    print(buffer.value.decode('big5'))
