def Rate(origin, userInput):
    if not (isinstance(origin, str) and isinstance(userInput, str)):
        print('The two parameters must be strings.')
        return
    if len(origin)<len(userInput):
        print('Sorry. I suppose the second parameter string is shorter.')
        return    
    right = 0					#精確符合的字元個數
    for origin_char, user_char in zip(origin, userInput):
        if origin_char==user_char:
            right += 1
    return right/len(origin)

origin = 'Shandong Institute of Business and Technology'
userInput = 'ShanDong institute of business and technolog'
print(Rate(origin, userInput))	#輸出測試結果
