#!/usr/bin/python3

from sys import exit
from text_multiplier import textMultiplier

output = textMultiplier("Ali Sorena", 2)
output = output.strip()
print(output)

if output.lower() == "alisorenaalisorena":
    print("Passed!")
    exit(0)
else:
    print("Failed!")    
    exit(1)