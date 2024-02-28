import re

def risedec(tex):
    sd = re.findall('[A-Z][a-z]+', tex)
    print(sd)

risedec('I WanT To Sleep VERy Much')


