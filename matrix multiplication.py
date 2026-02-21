# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 23:48:57 2026

@author: shubh
"""

result=0
mat1=[[5,8,6],[9,3,4],[8,5,2]]
mat2=[[4,5,6],[3,4,6],[6,2,4]]
for i in range(len(mat1)):
    for j in range(len(mat2)):
        for k in range(len(mat2)):
            result+=mat1[i][k]*mat2[k][j]
        print(result,end=" ")
        result=0
    print()    