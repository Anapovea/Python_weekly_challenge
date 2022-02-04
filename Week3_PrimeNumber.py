# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:50:01 2022
@author: Ana Povea
"""
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
# 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

def primeNumber(num):
    rang = range(89, 101,1)        
    for i in rang:
        prime = num % i == 0
        if prime:
            return print("Number", num, "is NOT Prime.", i) 
        else: 
            pass
    return  print("Number", num, "is Prime.", i) 

# Driver program
# num = i
# primeNumber(num)

#Print all Prime numbers from 1 to 100
print("****** Print all Prime numbers from 1 to 100 *******")


rang = range(2, 101,1)
for i in rang:
    primeNumber(i)
