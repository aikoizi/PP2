import re

def tex(text):
    s = 'a.*?b$'
    if re.search(s, text):
        print('Found a match')
    else:
        print('Not mached')

tex('asjdjdhdb')
