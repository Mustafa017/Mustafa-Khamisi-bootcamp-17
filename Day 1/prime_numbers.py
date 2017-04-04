# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:49:04 2017

@author: mustafa
"""
def prime_num(n):
    result = []
    for i in range(2,n+1):  #to loop between 2 upto n+1
       for j in range(2,i): #to loop over the factors of the number
          if i%j == 0:      #check if it has a factor
              break         #proceed to check next number
       else:
          result.append(i)
    print(result)
              
prime_num(200)