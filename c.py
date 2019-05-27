# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin
import itertools

import time
fd = open('c.txt')
stdin = fd
start=time.time()

############################################

import numpy as np
# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])
M = int(temp[1])

data = []
for i in range(M):
    write = stdin.readline().split()
    if int(write[0]) == 1:
        data.append(write[1])
    else:
        data.append(write[1:int(write[0])+1])

ans = stdin.readline().split()

count = 0

datas = data

data = [0,1]

M=N


if M == 1:
    a = list(itertools.product(data))
elif M == 2:
    a = list(itertools.product(data, data))
elif M == 3:
    a = list(itertools.product(data, data, data))
elif M == 4:
    a = list(itertools.product(data, data, data, data))
elif M == 5:
    a = list(itertools.product(data, data, data, data, data))
elif M == 6:
    a = list(itertools.product(data, data, data, data, data, data))
elif M == 7:
    a = list(itertools.product(data, data, data, data, data, data, data))
elif M == 8:
    a = list(itertools.product(data, data, data, data, data, data, data, data))
elif M == 9:
    a = list(itertools.product(data, data, data, data, data, data, data, data, data))
elif M == 10:
    a = list(itertools.product(data, data, data, data, data, data, data, data, data, data))
elif M == 11:
    a = list(itertools.product(data, data, data, data, data, data, data, data, data, data, data))

for element in a:
    for i, d in enumerate(datas):
        x = 0
        sum = 0
        if len(d) != 1:
            for dd in d:
               sum += element[int(dd)-1] 
        else:
           sum += element[int(d)-1]
           
        if sum%2 == int(ans[i]):
           continue
        else:
           x = 1
           break
       
    if x == 0:
        count+=1

print(count)
