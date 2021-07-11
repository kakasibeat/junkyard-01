# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 16:56:11 2021

@author: 愛場　隆之
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:46:44 2021

@author: 愛場　隆之
"""

import sympy
import random


def main():

    mode=int(input("mode選択 0:鍵生成 1:暗号化 2:複合化（未実装）"))
    if mode==0:
        make_key()
    elif mode==1:
        make_code()


def make_key():
    select=int(input("鍵の元になる2つの素数, 1:手動入力 2:乱数にお任せ  "))
    if select==1:
        p=int(input("pの値を入力してね"))
        q=int(input("qの値を入力してね"))
             
    elif select==2:
        lange=int(input("何桁欲しい？"))
        p=sympy.randprime(10**(lange-1),10**lange)
        q=sympy.randprime(10**(lange-1),10**lange)
        while p==q:
            q=sympy.randprime(10**(lange-1),10**lange)
        
    else:
        print("入力エラー")
    
        
    n=p*q
    
        
    L=(p-1)*(q-1)
    
        
    if p<q:
        MAX=q
    else:
        MAX=p
    e=int(input("eの値を入力してください、「０」入力でe=65537,「-1」入力でランダム生成"))
    if e==0:
        e=65537
    if e==-1:
        e=sympy.randprime(MAX,L)
            
    print("p=",p)
    print("q=",q)
    print("n=",n)
    print("L=",L)
    print("e=",e)

def make_code():
    """こっか暗号の中身の入力、予め数字に変換してもらう"""
    data=[]
    word=0
    code=[]
    rist=0
    i=0
    P=0
    e=int(input("eを入力してください"))
    n=int(input("nを入力してください"))
    
    while word!="end":
    
        word=(input("数値を入力してください、「end」で入力終了"))
            
        """数字が入力されたときのみリストに追加"""
        if word.isdigit()==True:
            data.insert(0,int(word))
            rist=rist+1 
            print("ok")
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




"""ランダムな整数を返す関数"""    
def r():
    a=random.random()*1000000//1
    return int(a)

main()
"なんか書いとけ"