# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:42:01 2024

@author: Hi
"""

a = float(input("Nhập điểm trung bình (GPA): "))
if a < 3.5:
    print("Học lực kém")
elif 3.5<= a <5.0:
    print("Học lực yếu")
elif 5.0<= a <7.0:
    print("Học lực trung bình")
elif 7.0<= a <8.0:
    print("Học lực khá")
elif 8.0<= a <9.0:
    print("Học lực giỏi")
elif 9.0<= a <=10.0:
    print("Học lực xuất sắc")