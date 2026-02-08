# -*- coding: utf-8 -*-
a=int(input("enter the year to be checked "))
if((a%4==0 and a%100!=0) or  (a%400==0)):
    print("the year is leap year ")
else:
    print("year is not leap year ")