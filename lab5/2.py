import re

def tex(text):
    sd = '^abb$'
    ds = '^abbb$'
    if re.search(sd, text) or re.search(ds, text):
        print('Found a match')
    else:
        print('Not matched')

tex('abb')
tex('abbb')
tex('abbbb')
