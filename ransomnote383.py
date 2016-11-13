# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:50:35 2016

@author: fang2
"""

def canConstruct(ransomNote, magazine):
    if len(ransomNote)==0:
        return True
    set1=set(ransomNote)
    set2=set(magazine)
    dict1=dict()
    dict2=dict()
    for elem in set1:
        dict1[elem]=0
    for elem in set2:
        dict2[elem]=0
    for elem in ransomNote:
        dict1[elem]+=1
    for elem in magazine:
        dict2[elem]+=1
    for key in dict1:
        if key not in dict2:
            return False
        elif dict1[key]>dict2[key]:
            return False
    return True
            


ransomNote="fihjjjjei"

magazine="hjibagacbhadfaefdjaeaebgi"
print(canConstruct(ransomNote,magazine))