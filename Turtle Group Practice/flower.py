# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 06:48:36 2021

@author: 
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()