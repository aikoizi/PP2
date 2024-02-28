import re

def tex(text):
    sd = '^a(b*)$'
    if re.search(sd, text):
        return 'Found a match'
    else:
        return 'Not matched' 

print(tex("ab"))