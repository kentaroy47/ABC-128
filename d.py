# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin
import itertools
import time
fd = open('d.txt')
stdin = fd
start=time.time()

############################################

import numpy as np
# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])
K = int(temp[1])

data = []
write = stdin.readline().split()
for a in write:
    data.append(int(a))

steps = min(N, K)

# A.. 左から取る数
# B.. 右から取る数

An = range(K+1)

max = 0

for A in An:
    for B in range(steps-A+1):       
        small = K - A - B
#        print("A:",A,"B:",B,"small:",small)
        left = data[0:A]
        right = []
        if not B==0:
            right = data[-B:]
        left.extend(right)
        left = sorted(left)
#        print(left)
        # remove stuff
        for k in range(small):
#            print(k)
            try:
                if left[k] <= 0:
                    left[k] = 0
            except:
                continue
        
        add = sum(left)
#        print(add)
        if max < add:
            max = add
print(max)