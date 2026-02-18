# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 23:46:16 2026

@author: shubh
"""

n = int(input("Enter decimal number: "))
binary = ""

while n > 0:
    rem = n % 2
    binary = str(rem) + binary
    n = n // 2

print("Binary number =", binary)
