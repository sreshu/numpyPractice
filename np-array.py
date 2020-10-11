#https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array

    result=numpy.array(arr,dtype=float)
    return result[::-1]

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)