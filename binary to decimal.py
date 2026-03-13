# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 23:17:56 2026

@author: shubh
"""

n=int(input("enter the binary no "))
dec=0
temp=1
while n>0:
    rem=n%10
    dec=dec+rem*temp
    temp=2*temp
    n=n//10
print("the decimal no is ",dec)    