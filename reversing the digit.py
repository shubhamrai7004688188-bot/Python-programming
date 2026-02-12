# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 21:32:50 2026

@author: shubh
"""

n=int(input("enter the  no to be reversed "))
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10 
print("reversed no is ",rev)
if temp==n:
    print("the no is pallindrome ")
else:
    print("the no is not pallindrome ")
    
  
    
 