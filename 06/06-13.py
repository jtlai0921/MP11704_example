import os

file_list = os.listdir(".")
for filename in file_list:         
	pos = filename.rindex(".") 
	if filename[pos+1:] == "html":
		newname = filename[:pos+1]+"htm" 
		os.rename(filename, newname)
		print(filename+"更名為："+newname)
