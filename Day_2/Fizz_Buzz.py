# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:33:36 2017

@author: mustafa
"""

def soln(n):
    if n%15 == 0:
        return "FizzBuzz"
    elif n%5 == 0:
        return "Buzz"
    elif n%3 == 0:
        return "Fizz"
    else:
        return n