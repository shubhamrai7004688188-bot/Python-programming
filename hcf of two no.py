# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 22:15:08 2026

@author: shubh
"""

a=int(input("enter the first no "))
b=int(input("enter the second no "))
hcf=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
print("hcf is ",hcf)        