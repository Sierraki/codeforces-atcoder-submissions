from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate
import sys

input = sys.stdin.readline
def mii():
    return map(int, input().split())
def lmii():
    return list(map(int, input().split()))
def ii():
    return int(input())
def si():
    return input()[:-1]


n,m=mii()
cnt=defaultdict(list)
for _ in range(n):
    a,b=mii()
    cnt[a].append(b)
res=[[i, (sum(j)/len(j))] for i,j in cnt.items()]
res.sort()
for i,j in res:
    print(j)