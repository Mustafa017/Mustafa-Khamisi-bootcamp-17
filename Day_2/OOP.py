# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:59:42 2017

@author: mustafa
"""

import sys,collections
class Solution:
    def __init__(self):
        self.myStack = list()
        self.myQueue = collections.deque([])

    def enter_stack(self,char):
        self.myStack.append(char)
       
    def exit_stack(self) :
        return self.myStack.pop() 
        
    def enter_queue(self,char):
        self.myQueue.append(char)
    
    def exit_queue(self):
        return self.myQueue.popleft()

s =  input() #Read input s
obj = Solution() #create Solution class object
L = len(s)

for i in range(L):
    obj.enter_stack(s[i])
    obj.enter_queue(s[i])
    
isPalindrome = True
'''pop the first character from the stack and deque the first character from 
the queue then compare.'''

for i in range(L // 2):
    if obj.exit_stack() != obj.exit_queue():
        isPalindrome = False
        break
'''finally print whether s is palindrome or not'''
if isPalindrome:
    print('The word, '+s+' , is a Palindrome.')
else:
     print('The word, '+s+' , is not a Palindrome.')