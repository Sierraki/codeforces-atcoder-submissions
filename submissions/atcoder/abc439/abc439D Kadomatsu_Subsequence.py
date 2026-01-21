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


n = ii()
nums = lmii()


def fun(nums):
    ans = 0
    cnt = Counter()
    for i in range(n):
        cnt[nums[i]] += 1
        if i >= 2:
            cur = nums[i]
            if cur % 5 == 0:
                if cur // 5 * 3 in cnt and cur // 5 * 7 in cnt:
                    ans += cnt[cur // 5 * 3] * cnt[cur // 5 * 7]
    return ans

print(fun(nums)+fun(nums[::-1]))
