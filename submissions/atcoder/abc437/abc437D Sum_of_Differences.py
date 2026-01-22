from collections import defaultdict, Counter, deque
from math import sqrt, floor
from bisect import bisect, bisect_left
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


n, m = mii()
nums1 = lmii()
nums2 = lmii()

ans = 0
nums2.sort()

pf = [0]
s = 0
for i in nums2:
    s += i
    pf.append(s)

for i in nums1:
    # print(i, bisect(nums2, i))
    tar = bisect(nums2, i)
    # p1 = nums2[:tar]
    # p2 = nums2[tar:]
    # print(p1, p2)
    ans -= pf[tar]
    ans += pf[-1] - pf[tar]
    ans += tar * i
    ans -= (m - tar) * i

print(abs(ans) % 998244353)
