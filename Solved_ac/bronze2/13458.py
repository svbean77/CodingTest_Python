#13458 시험 감독

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

admin = 0
for i in range(N):
    admin += 1
    A[i] -= B
    if A[i] > 0:
        admin += (A[i] // C)
        if A[i] % C != 0:
            admin += 1

print(admin)