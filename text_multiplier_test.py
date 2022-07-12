#!/usr/bin/python3

from sys import exit
from practice import textMultiplier

text = input("Enter your peiece of text : ")

number = input("How much : ")

output = textMultiplier(text, number)
if output == "Ali Sorena":
    print("Passed!")
    exit(10)
else:
    print("Failed!")    
    exit(1)