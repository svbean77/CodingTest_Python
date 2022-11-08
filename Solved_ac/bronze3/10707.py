#10707 수도요금

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
P = int(sys.stdin.readline())

cost1 = A * P
cost2 = B
if P > C:
    P -= C
    cost2 += (P * D)

print(min(cost1, cost2))