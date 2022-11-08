#2455 지능형 기차

import sys

people = 0
maxPeople = 0

for _ in range(4):
    o, i = map(int, sys.stdin.readline().split())
    people = people - o + i
    if people > maxPeople:
        maxPeople = people

print(maxPeople)