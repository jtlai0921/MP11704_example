with open('sample.txt') as fp:
    while True:
        line = fp.readline()
        if not line:
            break
        print(line)
