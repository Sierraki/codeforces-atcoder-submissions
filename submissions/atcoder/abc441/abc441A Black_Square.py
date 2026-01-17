import sys

input = sys.stdin.readline
# data = iter(sys.stdin.read().split())

p, q = map(int, input().split())
x, y = map(int, input().split())

a = p + 100 - 1 if p + 100 - 1 >= 0 else 0
b = q + 100 - 1 if q + 100 - 1 >= 0 else 0

if p <= x <= a and q <= y <= b:
    print("Yes")
else:
    print("No")
