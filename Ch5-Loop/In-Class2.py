# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 08:51:21 2021

@author: Relic
"""

##Print Multiplation Table

###Goal 1: Print 1 Row
#for columnIndex in range(1,10):
#    print(1*columnIndex,end='  ')
#    
# ##Goal 2: Print 2 Row
#for columnIndex in range(1,10):
#    print(2*columnIndex,end='  ')   
#
###Goal 3: Print 3 Row
#for columnIndex in range(1,10):
#    print(3*columnIndex,end='  ') 

##All Rows together   
for rowIndex in range(1,10):
    for columnIndex in range(1,10):
        if columnIndex == 5:
            break

        print(f'{rowIndex*columnIndex:4d}',end='  ') 
    print()

    