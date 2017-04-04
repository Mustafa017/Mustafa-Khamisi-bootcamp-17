# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:53:41 2017

@author: mustafa
"""

def data_type(n):
    if isinstance(n,str):
        return len(n)
    elif isinstance(n,bool):
        return n
    elif isinstance(n,int):
        if n == 100:
            return "Equal to 100"
        elif n > 100:
            return "more than 100"
        else:
            return "Less than 100"
    elif isinstance(n,list):
        if len(n) >= 3:
            return n[2]
        else:
            return None
    else:
        return "no value"
        
print(data_type([2,4]))