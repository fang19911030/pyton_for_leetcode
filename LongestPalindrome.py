# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 10:42:32 2016

@author: Pengcheng
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_dict=dict()
        keys=set(s)
        a=0
        b=0
        for elem in keys:
            string_dict[elem]=[]
        for i in range(len(s)):
            string_dict[s[i]].append(1)
        for key in string_dict.keys():
            string_dict[key]=sum(string_dict[key])
        for key in string_dict.keys():
            if string_dict[key]%2==1:
                a=1
                b+=string_dict[key]-1
            elif string_dict[key]%2==0:
                b+=string_dict[key]
                
        return a+b