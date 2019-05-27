# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('a.txt')
stdin = fd
start=time.time()

############################################


# read data for n sequences.
n = stdin.readline().split()
a = int(n[0])
b = int(n[1])

#data = [int(stdin.readline().rstrip()) for _ in range(n)]

out = int((a*3+b) / 2)

print(out)

#end = time.time()
#print(end-start)