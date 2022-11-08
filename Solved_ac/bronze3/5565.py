#5565 영수증

import sys
total = int(sys.stdin.readline())

for _ in range(9):
    cost = int(sys.stdin.readline())
    total -= cost

print(total)