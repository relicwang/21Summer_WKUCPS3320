# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 08:45:34 2021

@author: Relic
"""
#Range function with 1 args
list = range(5)  #--> [0,endVal-1]

#for i in list:
#    print(i)


#Range function with 2 args
list = range(5,11)  #--> [begVal,endVal-1]
#for i in list:
#    print(i)
#    
#Range function with 3 args
list = range(5,11,3)  #--> [begVal, endVal-1, step]
#for i in list:
#    print(i)
    
list = range(10,1,-2)  #--> [begVal, endVal-1, step]
#for i in list:
#    print(i)

#import math
##Compute squart root of values [1,100]
#for i in range(1,101):
#    print(f'Square root of {i} is {math.sqrt(i)}')
    


#Test with == and is





list1 = [1,5,8]
list2 = list1
del list
list3 = list(list1)
list5 = [1,5,8]


print(id(list1))
print(id(list2))
print(id(list3))
print(id(list5))
print('list1==list2', list1==list2)
print('list1==list3', list1==list3)

print('list1 is list2', list1 is list2)
print('list1 is list3', list1 is list3)
s1 = 'abc'
s2 = 'abc'
s3 = 'a'+'bc'


print(id(s1))
print(id(s2))
print(id(s3))





