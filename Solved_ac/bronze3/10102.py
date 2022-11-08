#10102 개표

import sys

V = int(sys.stdin.readline())
vote = list(sys.stdin.readline().strip())

A = 0
B = 0
for v in vote:
    if v == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")