#!/usr/bin/env python3
import sys
from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('rockyou.txt'))
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = input("Please specify path to dictionary:")
if len(sys.argv) > 2:
    num = sys.argv[2]
else:
    num = input("Please specify number of characters: ")
n = int(num)
with open(r""+path, encoding="latin-1") as file: 
    allText = file.read() 
    words = list(map(str, allText.split())) 
name =("rockyou_"+num+"_ch.txt")    
new_file= open(name,"w")
for j in words:
    if len(j)==n:
        new_file.write(j+"\n")        
file.close()
new_file.close()
print("\nFinished:")
print("rockyou_"+num+"_ch.txt was succesifuly created !\n")


