from ctypes.wintypes import *
from ctypes import *

kernel32 = windll.kernel32

class tagPROCESSENTRY32(Structure):	#定義結構體
    _fields_ = [('dwSize',		DWORD),
             ('cntUsage',			DWORD),
             ('th32ProcessID',		DWORD),
             ('th32DefaultHeapID',	POINTER(ULONG)),
             ('th32ModuleID',		DWORD),
             ('cntThreads',			DWORD),
             ('th32ParentProcessID',	DWORD),
             ('pcPriClassBase',		LONG),
             ('dwFlags',			DWORD),
             ('szExeFile',			c_char * 260)]
def killProcess(processNames):
    #建立處理程序快照
    hSnapshot = kernel32.CreateToolhelp32Snapshot(15, 0)
    fProcessEntry32 = tagPROCESSENTRY32()
    if hSnapshot:
        fProcessEntry32.dwSize = sizeof(fProcessEntry32)
        hasmore = kernel32.Process32First(hSnapshot, byref(fProcessEntry32))
        #列舉處理程序
        while hasmore:
            #可執行檔
            processName = (fProcessEntry32.szExeFile)
            #處理程序ID
            processID = fProcessEntry32.th32ProcessID
            if processName.decode().lower() in processNames:
                #取得處理程序控制碼
                hProcess = kernel32.OpenProcess(1, False, processID)
                #結束處理程序
                kernel32.TerminateProcess(hProcess,0)
            #取得下一個處理程序
            hasmore = kernel32.Process32Next(hSnapshot, byref(fProcessEntry32))

#待刪除的處理程序清單
processNames = ('notepad.exe', 'mspaint.exe')
killProcess(processNames)
