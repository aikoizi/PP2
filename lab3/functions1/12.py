def histogram(lis):
    s = ''
    for i in range(0, len(lis)):
        for x in range(0, lis[i]):
            x = '*'
            s += x
        print(s)
histogram([3,5,6])