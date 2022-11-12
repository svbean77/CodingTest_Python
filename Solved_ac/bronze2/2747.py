#2747 피보나치 수

import sys

n = int(sys.stdin.readline())

f2 = 0
f1 = 1
for _ in range(n):
    f2, f1 = f1, f1 + f2

print(f2)