# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:59:16 2024

@author: Hi
"""
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0: 
    if b == 0: 
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
print("Phương trình có nghiệm x:", x)
        
        

    