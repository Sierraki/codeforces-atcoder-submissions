from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
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
    return input().strip()


def lacc(nums):
    return list(acc(nums))


def solve():
    n = ii()
    nums = list(range(1, n + 1))
    res = []

    while len(nums) >= 2:
        cur1 = nums.pop()
        cur2 = nums.pop()
        if not res:
            res += [cur1, cur2] * cur2 + [cur1]
        else:
            res = [cur1] + res + [cur1, cur2] * cur2
    if nums:
        res.append(1)
    print(*res)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
