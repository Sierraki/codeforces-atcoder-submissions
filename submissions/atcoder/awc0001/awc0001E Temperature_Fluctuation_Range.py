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


def ms(numss):
    return "".join(map(str, numss))


def solve():
    n, k = mii()
    nums = lmii()

    mx = deque()
    mi = deque()
    ans = 0
    for i in range(n):
        while mx and nums[mx[-1]] <= nums[i]:
            mx.pop()
        mx.append(i)
        while mi and nums[mi[-1]] >= nums[i]:
            mi.pop()
        mi.append(i)
        if mx[0] < i - k + 1:
            mx.popleft()
        if mi[0] < i - k + 1:
            mi.popleft()
        if i >= k - 1:
            cur = nums[mx[0]] - nums[mi[0]]
            if cur > ans:
                ans = cur

    print(ans)


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
