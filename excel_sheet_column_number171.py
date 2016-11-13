# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:16:32 2016

@author: fang2
"""

def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    length=len(s)
    base=ord('A')
    result=0
    for i in range(length):
        result+=(ord(s[i])-base+1)*(26**(length-i-1))
        
    return result
    
s="A"
s2="AA"
print (titleToNumber(s))
print (titleToNumber(s2))