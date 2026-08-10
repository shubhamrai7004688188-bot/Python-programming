# -*- coding: utf-8 -*-
a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
c=int(input("enter the value of c "))
D = b*b - 4*a*c
if D<0:
    print("the equation has complex roots ")
elif D==0:
    print("the equation has same roots ")
else:
    print("the equation has real and distinct  roots ")
