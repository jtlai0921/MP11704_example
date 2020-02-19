def hannuo(num, src, dst, temp=None):
    #宣告用來記錄移動次數的變數為全域變數
    global times
    #確認參數類型和範圍
    assert type(num) == int, 'num must be integer'
    assert num > 0, 'num must > 0'
    #只剩最後或只有一個盤子需要移動，這也是函數遞迴呼叫的結束條件
    if num == 1:
        print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
        times += 1
    else:
        #遞迴呼叫函數本身，
        #先把除了最後一個盤子之外的所有盤子，移動到臨時柱子上
        hannuo(num-1, src, temp, dst)
        #把最後一個盤子直接移動到目標柱子上
        hannuo(1, src, dst)
        #把除了最後一個盤子之外的其他盤子，從臨時柱子上移動到目標柱子上
        hannuo(num-1, temp, dst, src)
#用來記錄移動次數的變數
times = 1
#A表示最初放置盤子的柱子，C是目標柱子，B是臨時柱子
hannuo(3, 'A', 'C', 'B')
