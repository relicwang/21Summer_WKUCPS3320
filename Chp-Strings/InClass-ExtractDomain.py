# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 09:28:34 2021

@author: Relic
"""

#Goal: Extract the domain info from given string


##1. Orignal String
#message='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
message='From jack@wku.edu.cn Sat Jan  5 09:14:16 2008'

##2. Get index of '@' -->atPos
atPos=message.find('@')

##3. Get index of space -' ' immediately after the '@' -->sepPos
sepPos=message.find(' ',atPos)


##4. Extract the domain:  message[atPos, sepPos]
domain = message[atPos+1:sepPos]

print(domain)


