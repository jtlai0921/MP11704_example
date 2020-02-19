numbers = []
while True:
    x = input('請輸入一個整數：')
    try:						#異常處理結構的相關細節，詳見第7章
        numbers.append(int(x))
    except:
        print('不是整數')
    while True:
        flag = input('繼續輸入嗎？（yes/no）')
        if flag.lower() not in ('yes', 'no'):	#限定輸入的內容必須為yes或no
            print('只能輸入yes或no')
        else:
            break
    if flag.lower()=='no':
        break

print(sum(numbers)/len(numbers))
