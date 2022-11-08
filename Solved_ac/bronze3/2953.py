#2953 나는 요리사다

import sys

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

maxScore = sum(lst[0])
winner = 1

for i in range(1, 5):
    if sum(lst[i]) > maxScore:
        maxScore = sum(lst[i])
        winner = i + 1

print(winner, maxScore)