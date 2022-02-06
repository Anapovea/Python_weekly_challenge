# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:35:38 2022
@author: Ana
"""
# Missing number in array
# Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

# Example 1:
# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4

# Example 2:
# Input:
# N = 10
# A[] = {6,1,2,8,3,4,7,10,5}
# Output: 9


def MissingNumber(array,n):
    #New array to compare
    array_new = list(range(1, n+2))
    # print(type(array_new))
    # print("length array_new", len(array_new))
    # length=len(array_new)
    print("The new array for this n is:", array_new)    

    for i in range (n):
        flag=0
        for j in range (n):           
            if array[j] == array_new[i]:
                pass #print("d", i,j, array[i])
                flag=1
            else:
                pass #print("ddd" ,array[i], array_new[j])
                # flag=0
        if flag == 0:
            print("prueba salida", array_new[i])
    return   
        # j=0
        # while j<n+1:
        #     # print("j=",j)
        #     # print("array ",array[i])
        #     # print("array new",array_new[j])
        #     if array[i] == array_new[j]:                 
        #         print("The missing number is not", array_new[j])
        #         # print(i)  
        #         pass
        #     # elif array[i] not array_new[j]:
        #     #     pass# print("prueba", array_new[j], array[i])
        #     else: 
        #         pass # print("d",array_new[j])
             
        #         # print("The not missing number is", array_new[j])
        #         # print("The missing number is", array_new[j])
        #     j+=1    
         

# Driver Code
array = [1,2,3,4,5,6,7,8,9,11]
n=len(array)       #n=4
print(MissingNumber(array, n))
    
    # array_list = list(array)
    # print(type(array_list))
    # for i in range (n):
    #      if i not in array_list and i!=0:
    #             print("The missing number is", i)
    # return i
