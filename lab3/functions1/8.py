def spy_game(listok):
    for i in range(len(listok)):
        if i==len(listok)-1:
                return False
        if listok[i]==0:
            for x in range(i+1,len(listok)):
                if x==len(listok)-1:
                    return False
                if listok[x]==0:
                    for k in range(x+1,len(listok)):
                        if listok[k]==7:
                            return True
                        if k==len(listok)-1:
                            return False