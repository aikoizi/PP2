def prime_n(num):
    num1 = []
    for i in range(0, len(num)):
        for x in range(2, num[i]):
            if num[i] == 2:
                num1.append(num[i])
                break
            if num[i] % 2 != 0:
                num1.append(num[i])
                break
            else:
                continue
    print(num1)
        
num = [8, 6 , 7, 4, 9, 3]
prime_n(num)