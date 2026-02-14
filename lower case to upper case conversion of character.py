# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 22:24:31 2026

@author: shubh
"""

a=input("enter the string ")
upper_case=""
lower_case=""
for ch in a:
      if("a"<=ch<="z"):
              upper_case+=chr(ord(ch)-32)
      
      else:
          upper_case+=ch
for ch in a:          
      if("A"<=ch<="Z"):
          lower_case=chr(ord(ch)+32)
      else:
          lower_case+=ch
print(upper_case)          
print(lower_case)