from ctypes import *
from time import sleep
from datetime import datetime

#方便呼叫Windows底層API函數
user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi

#即時查看目前視窗
def getProcessInfo():
    global windows
    #取得目前位於桌面最頂端的視窗控制碼
    hwnd = user32.GetForegroundWindow()
    pid = c_ulong(0)
    #取得處理程序ID
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    processId = str(pid.value)
    #取得可執行檔名稱
    executable = create_string_buffer(512)
    h_process = kernel32.OpenProcess(0x400|0x10, False, pid)
    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
    #取得視窗標題
    windowTitle = create_string_buffer(512)
    user32.GetWindowTextA(hwnd, byref(windowTitle), 512)
    #關閉控制碼
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    #更新最近兩個視窗清單
    windows.pop(0)
    windows.append([executable.value.decode('big5'),windowTitle.value.decode('big5')])

def main():
    global windows
    windows = [None, None]
    while True:
        getProcessInfo()
        #如果使用者切換視窗，則進行提示
        if windows[0] != windows[1]:
            print('='*30)
            print(str(datetime.now())[:19],windows[0],'==>',windows[1])
        sleep(0.2)
if __name__ == '__main__':
    main()
