#!/usr/bin/python3

#text multiplier

from sys import exit



def textMultiplier(text, number):
    if not text == "" or not number == "": 
        if not number.isnumeric():
            print("Enter a number...")
            exit(1)    
        else:
            return text * int(number)
    else:
        print("Don't leave it empty!") 
        exit(1)