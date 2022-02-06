# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:54:55 2022
@author: Ana Pov. 
"""
# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
# Fn = Fn-1 + Fn-2
# with seed values 
# F0 = 0 and F1 = 1.
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two that precede it.

# Write a function that takes an integer n and return the n-th Fibonacci number. 
# Sample input: 6
# Sample output: 5 (0,1,1,2,3,5)

# Input  : n = 9
# Output : 21 (0,1,1,2,3,5,8,13,21)


#test
number=9

def fibo_function (number): 
    if number < 0:
         print("Not posible")
    elif number == 0:
        return 0
    elif number == 1:
         return 0
    elif number <=3:
        return 1
    else:
        return fibo_function(number-1)+fibo_function(number-2)
    # print(fibo_function)

#Calling the function      
print(fibo_function(number))

#We have used recursion. The process in which a function calls
# itself directly or indirectly is called recursion and 
# the corresponding function is called as recursive function


      
