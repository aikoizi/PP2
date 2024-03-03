def risedec(text):
    cnt1 = 0
    cnt2 = 0
    for i in text:
        if i.isupper():
            cnt1+= 1
        elif i.islower():
            cnt2+= 1
    print("Number of upper case letters:", cnt1)
    print("Number of lower case letters:", cnt2)

risedec('KekUik')