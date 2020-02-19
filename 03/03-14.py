def licai(base, rate, days):
    result = base				#初始投資金額
    times = 365//days			#整除，用來計算一年可以滾動多少期
    for i in range(times):
        result = result +result*rate/365*days
    return result
print(licai(100000, 0.0385, 14))	#14天理財，利率0.0385，投資10萬
