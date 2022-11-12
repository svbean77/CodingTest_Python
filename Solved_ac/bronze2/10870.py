#10870 피보나치 수 5

import sys

n = int(sys.stdin.readline())

Fn_2 = 0
Fn_1 = 1

if n == 0:
    Fn = 0
elif n == 1:
    Fn = 1
else:
    for _ in range(n - 1):
        Fn = Fn_1 + Fn_2
        Fn_2, Fn_1 = Fn_1, Fn

print(Fn)