# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:46:44 2021

@author: 愛場　隆之
"""

import sympy
import random

"""ランダムな整数を返す関数"""
def r():
    a=random.random()*1000000//1
    return int(a)


p=r()
q=r()
n=p*q

print(p)
print(q)
print(n)

L=(p-1)*(q-1)
print(L)