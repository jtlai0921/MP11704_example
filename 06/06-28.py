from docx import Document
import re

result = {'li':[], 'fig':[], 'tab':[]}
doc = Document(r'd:\doc\05.docx')

for p in doc.paragraphs:			#遍歷檔案所有段落
    t = p.text					#獲得每一段的文字
    if re.match('例\d+-\d+ ', t):	#例題
        result['li'].append(t)
    elif re.match('圖\d+-\d+ ', t):	#插圖
        result['fig'].append(t)
    elif re.match('表\d+-\d+ ', t):	#表格
        result['tab'].append(t)

for key in result.keys():		#輸出結果
    print('='*30)
    for value in result[key]:
        print(value)
