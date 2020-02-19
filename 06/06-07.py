fp = open('sample.txt')

result = [0, '']
for line in fp:
    t = len(line)
    if t > result[0]:
        result[0] = t
        result[1] = line
fp.close()

print(result)
