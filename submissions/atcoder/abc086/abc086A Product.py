import sys
input=sys.stdin.readline
data=iter(input().split())
a, b = int(next(data)), int(next(data))
res=a*b
if res%2==0:
    print('Even')
else:
    print('Odd')
