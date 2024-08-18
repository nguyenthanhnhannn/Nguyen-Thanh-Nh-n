# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:24:36 2024

@author: Hi
"""

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and b + c > a and a + c > b: 
    print("Đây là 3 cạnh của tam giác")
else: 
    print("Đây không phải là 3 cạnh của tam giác")
    