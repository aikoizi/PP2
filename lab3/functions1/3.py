def solve(numheads,numlegs):
    chik = (numlegs - 2*numheads) /2 
    rabbi = numheads - chik
    rabbi=int(rabbi)
    chik=int(chik)
    return rabbi,",", chik

print(*solve(35,94))