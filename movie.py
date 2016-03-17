'''
for movie fun
'''
import re
import os
import time
print __name__

fp=open("./expression.txt","r+")
content=fp.read()
pattern=re.compile(r'[\u4e00-\u9fff]+',re.I)
content=re.sub(pattern,"",content)

pattern=re.compile(r"\d{2,}\.(.*?)\d{2}",re.I)
rs=re.findall(pattern,content)

print("a film of lucky")
time.sleep(2)
print("face expression")
time.sleep(2)
for e in rs:
    print(e)
    time.sleep(1)
time.sleep(3)
print("TNAHKS FOR WATCHING")
time.sleep(3)
print("DIRECTED BY LUCKY")
time.sleep(3)

