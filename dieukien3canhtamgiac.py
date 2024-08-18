# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:43:08 2024

@author: Hi
"""

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and b + c > a and a + c > b: 
    if a == b and b == c and c == a: 
        print("Đây là tam giác cân") 
    elif a == b == c: 
        print("Đây là tam giác đều") 
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a: 
        print("Đây là tam giác vuông") 
    else: 
        print("Đây là tam giác thường") 
else:
    print("Đây không phải là 3 cạnh của tam giác")
    