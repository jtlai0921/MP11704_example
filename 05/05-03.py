import re

telNumber = '''Suppose my Phone No. is 0535-1234567, yours is 010-12345678, his is 025-87654321.'''
pattern = re.compile(r'(\d{3, 4})-(\d{7, 8})')
index = 0
while True:
    matchResult = pattern.search(telNumber, index)		#從指定位置開始比對
    if not matchResult:
        break
    print('-'*30)
    print('Success:')
    for i in range(3):
        print('Searched content:', matchResult.group(i),\
        ' Start from:', matchResult.start(i), 'End at:', matchResult.end(i),\
          ' Its span is:', matchResult.span(i))
    index = matchResult.end(2)			#指定下次比對的開始位置
