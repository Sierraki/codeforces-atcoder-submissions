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
    adj = [[] for _ in range(n + 1)]
    # print(nums)

    for i, j in enumerate(nums, 1):
        adj[j].append(i)

    # print(adj)
    res = []
    vis = [False] * (n + 1)

    def dfs(cur, path):
        if not vis[cur]:
            path.append(cur)
            vis[cur] = True
            for i in adj[cur]:
                dfs(i, path)

    for i in nums[::-1]:
        if not vis[i]:
            path = []
            dfs(i, path)
            res.append(path[:])

    # print(res)
    ans = [0] * (n + 1)
    for i in res:
        for j in i:
            ans[j] = i[0]
    print(*ans[1:])


sys.setrecursionlimit(500000)
if __name__ == "__main__":
    # size = ii()
    # for _ in range(size):
    solve()
