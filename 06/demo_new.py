filename = 'demo.py'                                        #1
with open(filename, 'r') as fp:                             #2
    lines = fp.readlines()                                  #3
maxLength = max(map(len,lines))                             #4
for index, line in enumerate(lines):                        #5
    newLine = line.rstrip()                                 #6
    newLine = newLine + ' '*(maxLength+5-len(newLine))      #7
    newLine = newLine + '#' + str(index+1) + '\n'           #8
    lines[index] = newLine                                  #9
with open(filename[:-3]+'_new.py', 'w') as fp:              #10
    fp.writelines(lines)                                    #11
