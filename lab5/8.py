import re
s = "hdjGddMamaPop"
m = re.findall('[A-Z][^A-Z]*', s)
print(m)