def unique_elements(lis):
    lis1 = []
    for i in lis:
        if i not in lis1:
            lis1.append(i)
    return lis1


