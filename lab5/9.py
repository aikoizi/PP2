import re

def tex(text):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(tex("PochtiNemnogo"))