# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:53:22 2016

@author: Pengcheng
"""

def reverseString1(string):
    temp=[]
    result=""
    for elem in string:
        temp.append(elem)
    while len(temp)!=0:
        result=result+temp.pop()
    return result
    
string="abcdefghigh"
result=reverseString1(string)
print (result)        