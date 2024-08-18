# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:05:02 2024

@author: Hi
"""

n = float(input("Nhập quãng đường đi được (km): "))
if n<= 1: 
    print("Số tiền là 20k")
elif n<=3:
    print ("số tiền taxi đi được là : ", n*13 ,"k")
elif 4<=n<=8:
    print ("số tiền taxi đi được là : ", 3*13+(n-3)*12 ,"k")
elif n>8 and n<=100 :
    print ("số tiền taxi đi đc là : ", 3*13+5*12+(n-8)*10, "k")
else : 
    print("số tiền taxi đi được là : ", (3*13+5*12+(n-8)*10)-((3*13+5*12+(n-8)*10)*(8/100)), "k")
    