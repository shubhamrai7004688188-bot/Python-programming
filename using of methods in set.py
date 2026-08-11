# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 12:28:21 2026

@author: shubh
"""

set1={1,2,5,4,3}
set2={6,7,8,9}
set3={1,2}
if set1.isdisjoint(set2):
    print("set1 is disjoint of set2")
else:
    print("not a disjoint set")
if set3.issubset(set1):
    print("set3 is subset of set1")
else:
    print("not a subset")
if set1.issuperset(set3):
    print("set1 is superset of set 3")
else:
     print("not a superset")
    
    
    
    