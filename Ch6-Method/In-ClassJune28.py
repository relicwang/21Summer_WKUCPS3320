# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:11:38 2021

@author: Relic
"""

var1 = 5

def m1():
#    var1=1
    global var1
    var1+=1 # var1 = var1 +1
    print(var1)
    
m1()
print(var1)