# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:39:48 2024

@author: Hi
"""

d = int(input("Nhập ngày : "))
m = int(input("Nhập tháng : "))
y = int(input("Nhập năm : "))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 :
    x = True
else:
    x = False
if m in [1,3,5,7,8,10,12] :
    ngay = 31
elif m in [4,6,9,11] :
    ngay = 30
if m == 2 :
    if x :
        ngay = 29
    else :
        ngay = 28
if 1<= m <=12:
    if 1 <= d <= ngay:
        if x :
            print(f"{d}/{m}/{y} hợp lệ ")   
            print(f"{d}/{m}/{y} là năm nhuận") 
        else:
            print(f"{d}/{m}/{y} ko phải là năm nhuận")   
    else:
        print(f"{d}/{m}/{y}  không hợp lệ ")                    
else :
    print(f"{d}{m}{y}  không hợp lệ ")
