import tkinter
import tkinter.messagebox
import tkinter.ttk

#建立tkinter應用程式
root = tkinter.Tk()
#設定視窗標題
root.title('Selection widgets')
#定義視窗大小
root['height'] = 400
root['width'] = 320
#與姓名相關的變數
varName = tkinter.StringVar()
varName.set('')
#建立標籤，然後放到視窗上
labelName = tkinter.Label(root, text='Name:',justify=tkinter.RIGHT,width=50)
labelName.place(x=10, y=5, width=50, height=20)
#建立文字方塊，同時設定相關的變數
entryName = tkinter.Entry(root, width=120,textvariable=varName)
entryName.place(x=70, y=5, width=120, height=20)

labelGrade = tkinter.Label(root, text='Grade:', justify=tkinter.RIGHT, width=50)
labelGrade.place(x=10, y=40, width=50, height=20)
#模擬學生所在年級，字典鍵值為年級，屬性值為班級
studentClasses = {'1':['1', '2', '3', '4'],
               '2':['1', '2'],
               '3':['1', '2', '3']}
 #學生年級下拉式清單
comboGrade = tkinter.ttk.Combobox(root,width=50,
                              values=tuple(studentClasses.keys()))
comboGrade.place(x=70, y=40, width=50, height=20)
#事件處理函數
def comboChange(event):
    grade = comboGrade.get()
    if grade:
        #動態改變下拉式清單可選項目
        comboClass["values"] = studentClasses.get(grade)
    else:
        comboClass.set([])
#繫結下拉式清單事件處理函數
comboGrade.bind('<<ComboboxSelected>>', comboChange)

labelClass = tkinter.Label(root, text='Class:', justify=tkinter.RIGHT, width=50)
labelClass.place(x=130, y=40, width=50, height=20)
#學生年級下拉式清單
comboClass = tkinter.ttk.Combobox(root, width=50)
comboClass.place(x=190, y=40, width=50, height=20)

labelSex = tkinter.Label(root, text='Sex:', justify=tkinter.RIGHT, width=50)
labelSex.place(x=10, y=70, width=50, height=20)
#與性別相關的變數，1:男；0:女，預設為男
sex = tkinter.IntVar()
sex.set(1)
#單選鈕，男
radioMan = tkinter.Radiobutton(root,variable=sex,value=1,text='Man')
radioMan.place(x=70, y=70, width=50, height=20)
#單選鈕，女
radioWoman = tkinter.Radiobutton(root,variable=sex,value=0,text='Woman')
radioWoman.place(x=130, y=70, width=70, height=20)
#與是否為班長相關的變數，預設不是班長
monitor = tkinter.IntVar()
monitor.set(0)
#核取方塊，選中時變數值為1，未選中時變數值為0
checkMonitor = tkinter.Checkbutton(root,text='Is Monitor?', variable=monitor,
                              onvalue=1, offvalue=0)
checkMonitor.place(x=20, y=100, width=100, height=20)
#增加按鈕按一下事件處理函數
def addInformation():
    result = 'Name:' + entryName.get()
    result = result + ';Grade:' + comboGrade.get()
    result = result + ';Class:' + comboClass.get()
    result = result + ';Sex:' + ('Man' if sex.get() else 'Woman')
    result = result + ';Monitor:' + ('Yes' if monitor.get() else 'No')
    listboxStudents.insert(0, result)    
buttonAdd = tkinter.Button(root, text='Add',width=40, command=addInformation)
buttonAdd.place(x=130, y=100, width=40, height=20)
#刪除按鈕的事件處理函數
def deleteSelection():
    selection = listboxStudents.curselection()
    if  not selection:
        tkinter.messagebox.showinfo(title='Information', message='No Selection')
    else:
        listboxStudents.delete(selection)
buttonDelete = tkinter.Button(root, text='DeleteSelection',
                        width=100, command=deleteSelection)
buttonDelete.place(x=180, y=100, width=100, height=20)
#建立清單方塊
listboxStudents = tkinter.Listbox(root, width=300)
listboxStudents.place(x=10, y=130, width=300, height=200)
#啟動訊息迴圈
root.mainloop()
