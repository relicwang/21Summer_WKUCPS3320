# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 09:21:47 2021

@author: Relic
"""

##Signature: computeIncome: int int int -> int
##Purpose:   Compute the income based on 
##            given amount of seats for correspondings class,
##            where calss A -> 20, B -> 15, C -> 10
## Examples:
##          computeIncome(0,0,0) --> 0
##          computeIncome(1,2,3) --> 80
def computeIncome(classASeats,classBSeats,classCSeats):
    #1. Any seats number is negative int
    if classASeats<0 or classBSeats<0 or classCSeats<0:
        return 'invalid number'
  
    #2. Any other seat numbers
    SEAT_A_PRICE = 20
    SEAT_B_PRICE = 15
    SEAT_C_PRICE = 10

    return classASeats*SEAT_A_PRICE+classBSeats*SEAT_B_PRICE+classCSeats*SEAT_C_PRICE


##Test Cases:
## 1. Any seats number is negative int
assert computeIncome(-1,1,1) == 'invalid number'
assert computeIncome(2,-1,1) == 'invalid number'
assert computeIncome(2,1,-1) == 'invalid number'
assert computeIncome(-2,-1,1) == 'invalid number'
assert computeIncome(-2,1,-1) == 'invalid number'
assert computeIncome(2,-1,-1) == 'invalid number'
assert computeIncome(-2,-1,-1) == 'invalid number'

## 2. Any seats number is 0
assert computeIncome(0,1,1) == 25
assert computeIncome(1,0,1) == 30
assert computeIncome(1,1,0) == 35
assert computeIncome(0,0,1) == 10
assert computeIncome(1,0,0) == 20
assert computeIncome(0,1,0) == 15


## 3. Any other seat numbers
assert computeIncome(2,5,2) == 135
assert computeIncome(10,10,10) == 450
assert computeIncome(1,2,3) == 80

