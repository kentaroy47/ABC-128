# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('practice.txt')
stdin = fd
start=time.time()

############################################

import numpy as np
# read data for n sequences.
a = int(stdin.readline().split()[0])
n = stdin.readline().split()
b = int(n[0])
c = int(n[1])
word = str(stdin.readline().split()[0])

out1 = a+b+c

print(out1,word)