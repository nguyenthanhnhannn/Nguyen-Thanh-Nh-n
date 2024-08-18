# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:27:19 2024

@author: Hi
"""

n = float(input("hãy chọn kéo bấm 1, chọn búa bấm 2 hoặc chọn bao bấm 3 để chơi trò kéo búa bao: "))   
while n !=1  and n != 2 and n != 3 :
    print("sai cú pháp trò chơi! Xin hãy nhập lại")
    print('\n')
    n = float(input("hãy chọn kéo bấm 1, chọn búa bấm 2 hoặc chọn bao bấm 3 để chơi trò kéo búa bao: "))
import random
m = random.randint(1,3)
if n == 1 :
    print(" bạn ra: kéo")
    if m == 1 :
        print(" máy ra: bao")
        print(" kết quả: người thắng")
    elif m == 2 :
        print(" máy ra: kéo") 
        print(" kết quả: hoà")
    elif m == 3 :
        print("máy ra: búa")
        print("kết quả: máy thắng")
elif n == 2 :
    print(" bạn ra: búa")
    if m == 1 :
        print(" máy ra: bao")
        print(" kết quả: máy thắng")
    elif m == 2 :
        print(" máy ra: kéo") 
        print(" kết quả: người thắng")
    elif m == 3 :
        print("máy ra: búa")
        print("kết quả: hoà")
elif n == 3:
    print(" bạn ra: bao")
    if m == 1 :
        print(" máy ra: bao")
        print(" kết quả: hoà")
    elif m == 2 :
        print(" máy ra: kéo") 
        print(" kết quả: máy thắng")
    elif m == 3 :
        print("máy ra: búa")
        print("kết quả: Người Thắng")