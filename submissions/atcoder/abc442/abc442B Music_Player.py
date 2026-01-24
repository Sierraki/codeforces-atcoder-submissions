from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
from itertools import accumulate as acc
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


def lacc(nums):
    return list(acc(nums))


size = ii()
ans = 0
play = False

for i in range(size):
    # print(i)
    cur = ii()
    # print(cur)
    if cur == 1:
        ans += 1
    elif cur == 2:
        if ans >= 1:
            ans -= 1
    elif cur == 3:
        if not play:
            play = True
        else:
            play = False
    # print(ans, play)

    if ans >= 3 and play == True:
        print("Yes")
    else:
        print("No")
