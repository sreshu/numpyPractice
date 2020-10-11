#https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np
x=input().split()
print(np.array(x,dtype=int).reshape(3,3))