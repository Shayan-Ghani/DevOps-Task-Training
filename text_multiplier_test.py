#!/usr/bin/python3

from sys import exit
from text_multiplier import textMultiplier

text = textMultiplier("ALI SORENA, 3").lower()
output = ""
for i in range(len(text)):
    output += text[i].strip()
print(output)    
if output == "alisorenaalisorenaalisorena":
    print("passed")
    exit(0)
else:
    print("failed")    
    exit(1)