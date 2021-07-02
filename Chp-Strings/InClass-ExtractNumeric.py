# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 08:37:44 2021

@author: Relic
"""

#Goal: Extract the numberical part out from given string
#str = 'X-DSPAM-Confidence:0.8475'   -->0.8475

#1.Have a String
orgString = 'X-DSPAM-Confidence:0.8475' 

#2. Extract the substring which is numerical parts
##Idea: using the index of colon
colonIndex = orgString.find(':')
numericPart = orgString[colonIndex+1:]

#3. Convert the result to float
numericRst = float(numericPart)

print(numericRst)
print(type(numericRst))
