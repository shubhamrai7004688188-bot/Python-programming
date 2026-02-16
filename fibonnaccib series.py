# -*- coding: utf-8 -
n=int(input("enter no of terms "))
a=0
b=1
i=0
while i<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i=i+1
