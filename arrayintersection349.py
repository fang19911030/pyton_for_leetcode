# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:43:17 2016

@author: fang2
"""

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    set1=set(nums1)
    set2=set(nums2)
    result=[]
    for elem in set2:
        if elem in set1:
            result.append(elem)
            
    return result
    
    