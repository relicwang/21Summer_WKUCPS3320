# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 08:52:38 2021

@author: Relic
"""

###Match the grade based on the score given by user
##   <0.6 -> F
##   >=0.6 -> D
##   >=0.7 -> C
##   >=0.8 -> B
##   >=0.9 -> A

##Special Cases:
## 1. Score NOT numberic values
## 2. Scoce <0 OR Score>1
##  ----> Show bad score

##1. Get score from user

try:
    score   =   float(input("Score is:"))
    ##2.  Match the grade
    #print(score)
    if score<0 or score>1:
        print('Bad Score')
    else:
        if score < 0.6:
            print('F')
        elif score>=0.9:
            print('A')   
        elif score>=0.8:
            print('B')     
        elif score>=0.7:
            print('C')
        elif score>=0.6:
            print('D')

except:
     print('Bad Score')
     



