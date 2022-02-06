# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:55:59 2022
@author: AnaPov
"""
# Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number. 
# Examples : 

# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Output: Sum found between indexes 2 and 4
# Sum of elements between indices
# 2 and 4 is 20 + 3 + 10 = 33

# Algorithm:  

#     Traverse the array from start to end.
#     From every index start another loop from i to the end of array to
#     get all subarray starting from i, keep a variable sum to calculate the sum.
#     For every index in inner loop update sum = sum + array[j]
#     If the sum is equal to the given sum then print the subarray.

def subArraySum(arr,n,suma):
    for i in range(n):
        # suma=suma +arr[i]
        curr_sum=arr[i]
        # print("Sum of", i, "is", suma)
        # print("Current sum of", i, "is", arr[i])

        j=i+1
        while j<=n:
            
            if curr_sum==suma :
                print(curr_sum)
                print ("Sum found between indexes % d and % d" %( i, j-1))
                return 1
            if curr_sum > sum_: 
                break
            curr_sum = curr_sum + arr[j]
            j +=1

    print ("No subarray found")
    return 0 

# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)   #8
sum_ = 23
 
subArraySum(arr, n, sum_)
# Output
# Sum found between indexes 1 and 4             (2+4+8+9)