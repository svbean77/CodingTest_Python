#2530 인공지능 시계

A, B, C = map(int, input().split())
D = int(input())

#값이 매우 커 n분, n시간씩 증가할 수 있기 때문에
#증가하는 단위를 //60으로 설정하고 시간은 %24로 설정
C += (D % 60)
if C >= 60:
    tmp = C // 60
    B += tmp
    C %= 60
D //= 60
B += (D % 60)
if B >= 60:
    tmp = B // 60
    A += tmp
    B %= 60
D //= 60
A += D
if A >= 24:
    A %= 24

print(A, B, C)