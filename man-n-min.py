#https://www.hackerrank.com/challenges/np-min-and-max/forum

import numpy as np
n,m=map(int,input().split())
arr=np.array([input().split() for i in range(n)],dtype=int)
res=np.amin(arr,axis=1)
print(np.amax(res))