#https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy
N,M = list(map(int, input().split()))
l = []
for i in range(N):
    a = list(map(int, input().split()))
    l.append(a)
print(numpy.prod(numpy.sum(l, axis = 0)))