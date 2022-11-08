#2935 소음

import sys

A = int(sys.stdin.readline())
operator = sys.stdin.readline().strip()
B = int(sys.stdin.readline())

if operator == '+':
    print(A+B)
else:
    print(A*B)