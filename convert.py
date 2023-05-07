import helper
import os
import shutil
import sys

if len(sys.argv) < 2:
    print("Usage : python convert.py [filename]")
    sys.exit()

with open(sys.argv[1],'r',encoding='UTF8') as f:
    code = f.read()

oneliner = helper.loc('\n\nexec(' + repr(code) + ')')

with open('helper.py','r',encoding='UTF8') as k:
    helpers = k.read()

with open('stub.py','w',encoding='UTF8') as f:
    f.write(helpers+"\nexec(j(pa("+"'"+helper.ko(oneliner)+"')))")

print('[+] Generated stub.')