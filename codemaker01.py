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


p=283
q=317
n=p*q

print("p=",p)
print("q=",q)
print("n=",n)

L=(p-1)*(q-1)
print("L=",L)
e=3251

"""こっか暗号の中身の入力、予め数字に変換してもらう"""
data=[]
word=0
code=[]
rist=0
i=0
P=0
while word!="end":
    word=(input("数値を入力してください、「end」で入力終了"))
    
    """数字が入力されたときのみリストに追加"""
    if word.isdigit()==True:
        data.insert(0,int(word))
        rist=rist+1
n=int(input("ｎを設定してください"))
N=int(input("暗号の文字数は？"))

while i<rist:
    P=P+data[i]*(N**i)
    i=i+1

print("暗号化前の数値は",P)
j=P**e

C=j%n

print("暗号化後の数値は",C)

i=1
while C//(N**i)!=0:
    i=i+1

print(i)

while 0<i:
    i=i-1
    word=C//(N**i)
    code.append(word)
    C=C-word*(N**i)

print("暗号化後のデータは",code)