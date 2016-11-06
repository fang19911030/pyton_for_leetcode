# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:41:32 2016

@author: Pengcheng
"""
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    times=dict()
    thresold=len(nums)//2
    for elems in nums:
        times[elems]=[]
    for elems in nums:
       times[elems].append(1)
    for key in times.keys():
        if sum(times[key])>thresold:
            return key
            
nums=[1,2,3,4,5,5,5,5,5]
a=majorityElement(nums)
            
