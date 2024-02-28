import re

def low(tex):
    sd = re.findall('[a-z]_',tex)
    if sd:
        print(sd)
    else:
        print('No match')

low('b_s_hh,f')