#5543 상근날드

b = []
d = []

#버거 리스트
for _ in range(3):
    b.append(int(input()))

#음료 리스트
for _ in range(2):
    d.append(int(input()))

#각 리스트의 최소값을 더한 후 세트 할인값 제외
cost = min(b) + min(d) - 50

print(cost)