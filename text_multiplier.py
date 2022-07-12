#!/usr/bin/python3

#text multiplier

from sys import exit



def textMultiplier(text, number):

    text = input("Enter your peiece of text : ") + "/n"
    number = input("How much : ")

    if text == "" or number == "": 
        print("Don't leave it empty!")
        exit(1) 
    elif number.isnumeric() == False:
        print("Enter a number...")
        exit(1)    
    else:
        return text * int(number)
        exit(0)
        