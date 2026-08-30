# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 00:08:33 2026

@author: shubh
"""

a=input("enter the main string: ")
b=input("enter the substring: ")
count=0
m=len(a)
n=len(b)
for i in range(m-n+1):
    if a[i:i+n]==b:
        count+=1
print(count)        
        