from collections import defaultdict, Counter, deque
from math import sqrt, floor, gcd, ceil
from bisect import bisect, bisect_left
from itertools import accumulate as acc
import sys

input = sys.stdin.readline


def p(nums):
    for i in nums:
        print(i)


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
    n, m, l, s, t = mii()
    nums = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, c = mii()
        nums[u].append([v, c])

    # p(nums)
    res = set()

    def dfs(cur, path, cost):
        if len(path) > l + 1:
            return
        if len(path) == l + 1 and s <= cost <= t:
            res.add(path[-1])
            return

        for i in range(len(nums[cur])):
            path.append(nums[cur][i][0])

            dfs(nums[cur][i][0], path, cost + nums[cur][i][1])
            path.pop()
            # cost -= nums[cur][i][1]

    dfs(1, [1], 0)
    print(*sorted(list(res)))


sys.setrecursionlimit(200000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
