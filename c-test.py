# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('c.txt')
stdin = fd
start=time.time()

import sys
 
n, m = list(map(int, input().split()))
swi = []
for _ in range(m):
    k, *sss = list(map(int, input().split()))
    t = 0
    for s in sss:
        t += 1 << (s - 1)
    swi.append(t)
ppp = list(map(int, input().split()))
 
ans = 0
for i in range(1 << n):
    for s, p in zip(swi, ppp):
        t = i & s
        c = bin(t).count('1') % 2
        if c != p:
            break
    else:
        ans += 1
print(ans)