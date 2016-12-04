# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:12:30 2016

@author: fang2
"""

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
        stack=list()
        operator={"+","-","*","/"}
        for elem in tokens:
            if elem not in operator:
                stack.append(int(elem))
            elif elem=="+":
                a=stack.pop()
                b=stack.pop()
                result=a+b
                stack.append(result)
            elif elem=="-":
                b=stack.pop()
                a=stack.pop()
                result=a-b
                stack.append(result)
            elif elem=="*":
                a=stack.pop()
                b=stack.pop()
                result=a*b
                stack.append(result)
            else:
                b=stack.pop()
                a=stack.pop()
                result=int(a*1.0/b)
                stack.append(result)
        if len(stack)!=0:
            return stack[-1]

tokens1=["2","1","3","*"]
tokens2=["4","13","5","/","+"]
result1=evalRPN(tokens1)
result2=evalRPN(tokens2)