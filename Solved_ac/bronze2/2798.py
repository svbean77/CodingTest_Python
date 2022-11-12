#2798 블랙잭

import sys

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

optimal = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = (card[i] + card[j] + card[k])
            if (sum <= M) and (sum > optimal):
                optimal = sum

print(optimal)