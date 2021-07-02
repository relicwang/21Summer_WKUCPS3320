# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 08:42:48 2021

@author: Relic
"""

###Gaol: Implement min method with two numberic variavbles
##         return the one is smaller


#Signature:  min: float float -> float
#Purpose:    Compare two given float value,
#             and return the one is smaller
#Example:
#            min(1,2)->1
#            min(3.4,1.5)->1.5
#            min(-0.7,-1.3)->-1.3
#            min(1,-1)->-1
def min(num1, num2):
    if num1>num2:
        return num2
    else:
        return num1

#print(min(5,1))

##Test Case:
##1. #1 > #2
##    a. + +
assert min(5,1) == 1 
assert min(722,22) == 22

##    b. - -
assert min(-1,-5) == -5
assert min(-100,-101) == -101

##    c. + -
assert min(1,-5) == -5
assert min(100,-55) == -55

##2. #1 < #2
##    a. + +
assert min(20,25)  == 20
assert min(100,200)  == 100

##    b. - +
assert min(-10,5)  == -10
assert min(-20,6)  == -20

##    c. - -
assert min(-5,-4)  == -5
assert min(-10,-7)  == -10

##3. #1 == #2
##    a. +  +
assert min(5,5)  == 5
assert min(1000,1000)  == 1000

##    b. 0  0
assert min(0,0)  == 0

##    c. -  -
assert min(-4,-4)  == -4
assert min(-2.4,-2.4)  == -2.4