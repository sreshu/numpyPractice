#https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np
x=list(map(int,input().split()))
print(np.zeros(x,dtype=int))
print(np.ones(x,dtype=int))