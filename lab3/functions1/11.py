def palin(s = str(input())):
    s1 = s[::-1]
    if s1 == s:
        print('It is palindrome')
    else:
        print('It is not palindrome')
palin()