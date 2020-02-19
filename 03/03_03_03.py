def scope_test():
    def do_local():
        spam = "我是區域變數"

    def do_nonlocal():
        nonlocal spam		#這時要求spam必須是已存在的變數
        spam = "我不是區域變數，也不是全域變數"

    def do_global():
        global spam		#如果全域作用域沒有spam，就自動新建一個
        spam = "我是全域變數"

    spam = "原來的值"
    do_local()
    print("設定區域變數值後：", spam)
    do_nonlocal()
    print("設定nonlocal變數值後：", spam)
    do_global()
    print("設定全域變數值後", spam)

scope_test()
print("全域變數：", spam)
