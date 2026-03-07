import heapq

import sys

from bisect import bisect, bisect_left

from collections import Counter, defaultdict, deque

from functools import cache, lru_cache

from itertools import accumulate as acc

from math import ceil, floor, gcd, sqrt







input = sys.stdin.readline

# num

def ii(): return int(input())

def mii(): return map(int, input().split())

def lmii(): return list(map(int, input().split()))

# string

def lmsi(): return list(map(str, si()))

def si(): return input().strip()

def ms(numss): return "".join(map(str, numss))

# else

def lacc(nums): return list(acc(nums))

def matt(row, col): return [[0] * col for _ in range(row)]

def p(numss):

    for i in numss:

        print(i)

def read_mat(n): return [lmii() for _ in range(n)]



def solve():

    n = ii()

    nums = [0] + lmii()

    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):

        a, b =mii()

        adj[a].append(b)

        adj[b].append(a)

    ans = ["No"] * (n + 1)

    cnt = {}

    total = 0

    def dfs(u, p):

        nonlocal total

        val = nums[u]

        cur = cnt.get(val, 0)

        if cur == 1:

            total += 1

        cnt[val] = cur + 1



        if total > 0:

            ans[u] = "Yes"

        else:

            ans[u] = "No"

        for v in adj[u]:

            if v != p:

                dfs(v, u)

        if cnt[val] == 2:

            total -= 1

        cnt[val] -= 1

    dfs(1, -1)

    print('\n'.join(ans[1:]))

    pass



sys.setrecursionlimit(200000)

if __name__ == "__main__":

    # size = ii()

    # for _ in range(size):

    solve()