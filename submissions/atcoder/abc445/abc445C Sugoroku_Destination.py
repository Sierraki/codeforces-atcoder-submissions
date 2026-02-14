from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc
from functools import cache, lru_cache
import heapq
import sys

input = sys.stdin.readline


def mii():
    return map(int, input().split())


def lmii():
    return list(map(int, input().split()))


def ii():
    return int(input())


def si():
    return input().strip()


def lacc(nums):
    return list(acc(nums))


def ms(numss):
    return "".join(map(str, numss))


def solve():
    n = ii()
    nums = lmii()

    res = [0] * (n + 1)
    for i in range(n, -1, -1):
        if i == n:
            res[i] = nums[i - 1]
        else:
            cur = nums[i - 1]
            if not res[cur]:

                res[i] = cur
            else:
                res[i] = res[nums[i - 1]]

    print(*res[1:])


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
