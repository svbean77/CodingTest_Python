#2460 지능형 기차 2

import sys

crowd = 0
maxPeople = 0

for _ in range(10):
    o, i = map(int ,sys.stdin.readline().split())
    crowd = crowd + i - o
    if crowd > maxPeople:
        maxPeople = crowd

print(maxPeople)