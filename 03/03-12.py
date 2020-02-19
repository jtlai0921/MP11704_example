digits = (1, 2, 3, 4)
for i in digits:
    ii = i*100
    for j in digits:
        if j==i:
            continue
        jj = j*10
        for k in digits:
            if k==i or k==j:
                continue
            print(ii+jj+k)
