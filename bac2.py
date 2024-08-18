# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:11:23 2024

@author: Hi
"""
import math 
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b*b - 4*a*c 
if delta< 0:
 print("Phương trình vô nghiệm")
elif delta == 0: 
    x = -b / (2*a)
    print("Phương trình có nghiệm kép x1=x2: ",x)
else:  
    x1 = ( -b + math.sqrt(delta)) / 2*a
    x2 = ( -b - math.sqrt(delta)) / 2*a
    print("Nghiệm của phương trình x1:", x1)
    print("Nghiệm của phương trình x2:", x2)