def main():	#def是用來定義函數的Python關鍵字
    if __name__ == '__main__':		#選擇結構，識別目前執行方式
        print('This program is run directly.')
    elif __name__ == 'hello':		#冒號、換行、縮排表示一個語句區塊的開始
        print('This program is used as a module.')

main()		#呼叫上面定義的函數
