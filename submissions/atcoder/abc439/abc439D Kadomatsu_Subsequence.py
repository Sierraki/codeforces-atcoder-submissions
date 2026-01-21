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
ans = 0
cnt = Counter()
total = Counter(nums)
for i in range(n):
    cur = nums[i]

    cnt[cur] += 1
    total[cur] -= 1
    

    

    if cur % 5 == 0:
        if cur // 5 * 3 in cnt and cur // 5 * 7 in cnt:
            ans += cnt[cur // 5 * 3] * cnt[cur // 5 * 7]
        if cur // 5 * 3 in total and cur // 5 * 7 in total:
            ans += total[cur // 5 * 3] * total[cur // 5 * 7]

print(ans)
