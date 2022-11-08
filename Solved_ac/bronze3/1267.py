#1267 핸드폰 요금

import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

Y = 0
M = 0
for time in T:
    #경계값(30, 60)은 가격의 단위가 올라가기 때문에 +1
    #몫만큼 가격 추가
    #나머지 단위(1~29, 1~59) 추가 +1
    if time % 30 == 0:
        Y += 1
    Y += time // 30
    if time % 30 != 0:
        Y += 1

    if time % 60 == 0:
        M += 1
    M += time // 60
    if time % 60 != 0:
        M += 1

if Y * 10 < M * 15:
    print(f'Y {Y * 10}')
elif Y * 10 > M * 15:
    print(f'M {M * 15}')
else:
    print(f'Y M {Y * 10}')