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
    n = ii()
    nums = lmii()
    nums.sort()

    total = sum(nums)
    mx = nums[-1]
    res = []

    ans1 = (n + 1) // 2
    ans2 = n

    for k in range(ans1, ans2 + 1):
        if total % k == 0:
            cur = total // k
            if cur >= mx:
                l, r = 0, n - 1
                swap = True
                while l <= r:
                    if nums[r] == cur:
                        r -= 1
                    elif l < r and nums[r] + nums[l] == cur:
                        r -= 1
                        l += 1
                    else:
                        swap = False
                        break
                if swap:
                    res.append(cur)

    res.sort()
    print(*(res))


# sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
