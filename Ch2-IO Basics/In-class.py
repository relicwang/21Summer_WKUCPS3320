# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 08:36:01 2021

@author: Relic
"""
####Splite Statement
#x=1
#y=2
#z=3
#
##Add x, y, z
#x=x+y+\
#z
#
##Print new x
#print(x)

####Print Method
#x=1000000000.0222
##print('X is',x,sep=' ',end='\t')
##print('X is',x,sep=' ')
#
#print(f'{x:7,.2f}')
#print(x)


##### Compute Perimeter and area
#####  for the cricle where the radius is from user
#import math
#
##print(math.pi)
#
##Get radius from user
#radius = float(input("Enter the radius:"))
#
##Compute the perimeter and area
#perimeter = 2*math.pi*radius
#area      = math.pi*radius**2
#
##Print out the perimeter and are
#print(f'Perimeter is{perimeter: .3f}')
#print(f'Area is{area: .3f}')

###Compute materials(sugar, butter, flour) 
##   needed for making number of cookied required by user

#Variables for holding the needed materails and cookies
cookies = 0
sugar   = 0
butter  = 0
flour   = 0

#Variables specified in the recipe
COOKIEE_RECIPE = 48
SUGAR_RECIPE   = 1.5
BUTTER_RECIPE  = 1
FLOUR_RECIPE   = 2.75

#Get # of cookie from user
cookies = float(input('Number of cookies to make:'))

#Compute the sugar need
sugar = cookies*SUGAR_RECIPE/COOKIEE_RECIPE

#Compute the butter need
butter = cookies*BUTTER_RECIPE/COOKIEE_RECIPE

#Compute the flour need
flour = cookies*FLOUR_RECIPE/COOKIEE_RECIPE

#Show the material needed 
print(f'{cookies} pieces of cookie need:')
print(f'{sugar} cup of sugar')
print(f'{butter} cup of butter')
print(f'{flour} cup of flour')