from datetime import date

daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def myCalendar(year, month):
    #取得year年month月1日是周幾
    start = date(year, month, 1).timetuple().tm_wday
    #輸出表頭資訊
    print('{0}年{1}月日曆'.format(year,month).center(56))
    print('\t'.join('日 一 二 三 四 五 六'.split()))
    #取得該月有多少天，如果是2月並且是閏年，就適當調整一下
    day = daysOfMonth[month-1]
    if month==2:
        if year%400==0 or (year%4==0 and year%100!=0):
            day += 1
    #產生資料，根據需求在前面加上空白
    result = [' '*8 for i in range(start+1)]
    result += list(map(lambda d: str(d).ljust(8), range(1, day+1)))
    #列印資料
    for i, day in enumerate(result):
        if i!=0 and i%7==0:
            print()
        print(day, end='')
    print()
def main(year, month=-1):
    if type(year)!=int or year<1000 or year>10000:
        print('Year error')
        return
    if type(month)==int:
        #如果沒有指定月份，就列印全年的日曆
        if month==-1:
            for m in range(1, 13):
                myCalendar(year, m)
        #如果指定了月份，就只列印這一個月的日曆
        elif month in range(1,13):
            myCalendar(year, month)
        else:
            print('Month error')
            return
    else:
        print('Month error')
        return
main(2017)
