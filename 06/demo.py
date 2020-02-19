filename = 'demo.py'
with open(filename, 'r') as fp:
    lines = fp.readlines()
maxLength = max(map(len,lines))
for index, line in enumerate(lines):
    newLine = line.rstrip()
    newLine = newLine + ' '*(maxLength+5-len(newLine))
    newLine = newLine + '#' + str(index+1) + '\n'
    lines[index] = newLine
with open(filename[:-3]+'_new.py', 'w') as fp:
    fp.writelines(lines)
