#2845 파티가 끝나고 난 뒤

L, P = map(int, input().split())
people = list(map(int, input().split()))

maxPeople = P * L

for item in people:
    print(item - maxPeople, end = ' ')