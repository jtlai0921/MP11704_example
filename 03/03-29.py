def convert(YearMonthDay):
    if not isinstance(YearMonthDay, str):
        return 'Type Error. Must be str'
    if YearMonthDay.count('-') != 2:
        return 'Parameter Error. Must contains 2 -'
    data = YearMonthDay.split('-')
    if (len(data[0]) != 4) or (len(data[1]) not in (1, 2)) or (len(data[2]) not in (1, 2)):
        return 'Parameter Error. Must be YYYY-MM-DD'
    try:
        year, month, day = map(int, data)
        quarter = [[3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2]]
        for q, m in enumerate(quarter):
            if month in m:
                return str(year) + str(q+1)
    except:
        return 'Parameter Error. Must be YYYY-MM-DD, and all be digits'

print(convert('2016-a9-27'))
