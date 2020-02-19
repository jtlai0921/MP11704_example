from xlwt import *

book = Workbook()				#建立新的Excel檔案
sheet1 = book.add_sheet("First")	#增加新的worksheet
al = Alignment()
al.horz = Alignment.HORZ_CENTER	#對齊方式
al.vert = Alignment.VERT_CENTER
borders = Borders()
borders.bottom = Borders.THICK	#邊框樣式
style = XFStyle()
style.alignment = al
Style.borders = borders
row0 = sheet1.row(0)			#擷取第0行列
row0.write(0, 'test', style=style)	#寫入儲存格
book.save(r'D:\test.xls')		#儲存檔案
