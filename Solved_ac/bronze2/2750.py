#2750 수 정렬하기

import sys

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

for item in num:
    print(item)