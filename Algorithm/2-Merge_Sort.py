#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Problem: Sort an array of integers in ascending order.
Definition: Given an array of integers, sort the array
in ascending order using a divide and conquer approach.
The array is split in left and right recursively and
merged into a final ouput array by comparing the elements
in the left and right array and appending them to the output
based on increasing value.
Complexity: O(n log(n))
Usage:
    $ python3 -m doctest merge_sort.py
"""

def merge(L, R):
    result = []
    i , j = 0 , 0
    while i < len (L) and j < len (R):
        if L[i] <= R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1

    result += L[i:]
    result += R[j:]
    return result

def mergesort(A):
    if len(A) <= 1:
        return A

    middle = len(A) // 2
    L   = mergesort(A[:middle])
    R   = mergesort(A[middle:])
    
    return merge(L, R)

print(mergesort([100,2,33,5,3,14,3,33,2,4,7,8,9]))