# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:49:04 2017

@author: mustafa
"""
def prime_num(n):
    if n < 0:
        return "invalid input"  # accepts only positive numbers
    elif n < 2:
        return "0 and 1 are not prime" # 0 and 1 are not prime numbers
    else:
        result = []
        for i in range(2, n + 1):  # to loop between 2 upto n+1
            for j in range(2, i):  # to loop over the factors of the number
                if i % j == 0:  # check if it has a factor
                    break  # proceed to check next number
            else:
                result.append(i)
        return result