import os
import sys
from tkinter import Tk, Button
from tkinter import filedialog
from tkinter import simpledialog

try:
    import openpyxl
except:
    #先把pip升級到最新版本
    path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install --upgrade pip'
    os.system(path)
    #安裝openpyxl擴展庫
    path = '"'+os.path.dirname(sys.executable)+'\\scripts\\pip" install openpyxl'
    os.system(path)
    import openpyxl

def merge(start):
    #顯示開啟檔案對話方塊，開啟待合併的Excel 2007+檔
    opts= {'filetypes':[('Excel 2007', '.xlsx')]}
    filename = filedialog.askopenfilename(**opts)
    #如果未選擇檔案，便不執行後面的程式碼
    if not filename:
        return
    #分割路徑和檔案名稱
    filepath, tempfilename = os.path.split(filename)
    shotname = os.path.splitext(tempfilename)[0]
    #產生新的檔案名稱
    newFile = filepath + '\\' + shotname + '_merge.xlsx'
    #建立新的Excel 2007+檔案
    workbook = openpyxl.Workbook()
    #增加新的worksheet
    worksheet = workbook.worksheets[0]
    data = openpyxl.load_workbook(filename)
    for sheetnum, sheet in enumerate(data.worksheets):
        #根據設定的表頭列數，設定讀取的起始列
        #第一個sheet讀取表頭，後面的sheet忽略表頭
        if sheetnum == 0:
            rowStart = 0
        else:
            rowStart = start
        #遍歷原sheet，根據情況忽略表頭
        for row in sheet.rows[rowStart:]:
            line = [col.value for col in row]
            worksheet.append(line)
    #儲存新檔
    workbook.save(newFile)
    #開啟剛剛建立的新文件
    os.startfile(newFile)
    
#按一下按鈕後執行的函數，參數a表示Excel檔案每個worksheet預期的表頭列數
def callback():
    kw = {'initialvalue':1, 'minvalue':0, 'maxvalue':10}
    headerNum = simpledialog.askinteger('表頭列數', '請輸入表頭列數',**kw)
    if headerNum != None:
        merge(headerNum)
    
root = Tk()
root.title("合併sheet")
Button(root, text="合併WorkSheets", bg='blue', bd=2,width=28,command=callback).pack()

root.mainloop()
