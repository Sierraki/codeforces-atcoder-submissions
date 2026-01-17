import sys

input = sys.stdin.readline
# data = iter(sys.stdin.read().split())
# size = int(input())
# for _ in range(size):
#     n=int(input())
n, k, x = map(int, input().split())
nums = list(map(int, input().split()))

# print(n, k, x)
# print(nums)

nums.sort(reverse=True)
total = sum(nums)
water = sum(nums[: (n - k)])

wine = total - water

# print(water, wine)

cnt = n - k
if wine >= x:
    pin = n - k
    while x > 0:
        x -= nums[pin]
        pin += 1
        cnt += 1
    print(cnt)
else:
    print(-1)
