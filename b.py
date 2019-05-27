# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('b.txt')
stdin = fd
start=time.time()

############################################

import numpy as np
# read data for n sequences.
a = int(stdin.readline().split()[0])
n = []
for i in range(a):
    write = stdin.readline().split()
    n.append([write[0],-int(write[1]),i])
#    b = str(n[0])
#    c = int(n[1])
#word = str(stdin.readline().split()[0])

n2 = sorted(n, key=lambda x:(x[0], x[1]))


for el in n2:
    print(el[2]+1)