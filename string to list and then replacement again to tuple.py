# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 00:09:00 2026

@author: shubh
"""

str=("I love my India")
list=str.split()
print(list)
for i in range(len(list)):
    if list[i]=="I":
        list[i]="we"
    if list[i]=="my":
        list[i]="our"
print("the list after replacement",list)        
tuple=tuple(list)
print("immutable list",tuple)
s="".join(tuple)
print(s)