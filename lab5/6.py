import re

def tex(text):
    x = re.sub("\s", ",", text)
    y = re.sub('\.', ':', x)
    print(x)
    print(y)

tex("dd.jdh.ll")
#tex('hdh ks dd')