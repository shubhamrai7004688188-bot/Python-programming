# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:03:27 2026

@author: shubh
"""

n=int(input("enter the no you want to check"))

for i in range(2,n):
    count1=0
    count2=0
    for j in range (2,i+1):
        if i%j==0:
            count1+=1
    k=n-i
    for j in range(2,k+1):
        if k%j==0:
            count2+=1
         
    if count1==3 and count2==3:
       print("is sum of two semi prime no")
       i=0
       break
    count1=0
    count2=0
if i!=0:
    print("not a sum of semi prime no")

         