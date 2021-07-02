# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 09:42:56 2021

@author: Relic
"""
#Compute Payment
##Base Hour, overload rate
BASE_HOUR = 40
OVERLOAD_RATE = 1.5

try:
    ##Get Hours and Rate
    hour=float(input("Enter hours:"))
    rate=float(input("Enter rate:"))

    ##Compute the payment
    ##If hour>40, pay = BASE_HOUR*rate + (hour-BASE_HOUR)*rate*OVERLOAD_RATE
    ##If hou<=40, pay = hour*rate
    if hour>40:
        pay = BASE_HOUR*rate + (hour-BASE_HOUR)*rate*OVERLOAD_RATE
        
    else:
        pay = hour*rate
        
    print(f"Pay is {pay:.2f}")
except:
    print("Please enter the number")