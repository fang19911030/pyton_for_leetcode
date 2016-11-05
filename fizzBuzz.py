# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:03:38 2016

@author: fang2
"""


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result=[]
    for i in range(n):
        if (i+1)%15==0:
            result.append("FizzBuzz")
        elif (i+1)%3==0:
            result.append("Fizz")
        elif (i+1)%5==0:
            result.append("Buzz")
        else:
            result.append(str(i+1))
            
    return result
    
test=16
print (fizzBuzz(16))