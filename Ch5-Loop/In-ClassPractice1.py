# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:29:26 2021

@author: Relic
"""

##Goal: Keep ask user to give us a number
##       Compute the sum, average, and count 
##       Stop when user enter 'done'
##Special:
##      If input is not a number, show user
##        some hints and input again

##1. Define count, sum, average
count = 0 
total = 0
average = 0

print(1)

##2. Get input from user

userInput = input('Enter a number')
while userInput!='done':
    try:
        
        total+=float(userInput)
        count+=1
    except:
        print('Invalid Input')
        
    userInput = input('Enter a number')


##Print count, total, average
print(total,count,total/count)



