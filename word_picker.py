#!/usr/bin/env python3
import sys
from pyfiglet import Figlet
from tqdm import tqdm
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('rockyou.txt'))
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = print("Error: Path to wordlist was not specified.")
if len(sys.argv) > 2:
    num_1 = sys.argv[2]
else:
    print("Error: Number of characters was not specified.")
j=""
num_1_int = int(num_1)
name =("rockyou_"+num_1+"_ch.txt")
if len(sys.argv) > 3:
    num_2 = sys.argv[3]
    num_2_int = int(num_2)
    name =("rockyou_"+num_1+"-"+num_2+"_ch.txt")    
with open(r""+path, encoding="latin-1") as file: 
    allText = file.read() 
    words = list(map(str, allText.split()))     
new_file= open(name,"w")
for j in tqdm(words):
    if len(sys.argv) > 3:
        case = (num_1_int<=len(j)<=num_2_int)
    else:
        case = (len(j)==num_1_int)    
    if (case):
        new_file.write(j+"\n")        
new_file.close()
print("\nFinished:")
print(name+" was succesifuly created !\n")