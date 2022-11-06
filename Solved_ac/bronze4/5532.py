#5532 방학 숙제

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A % C != 0:
    A += C
if B % D != 0:
    B += D

day = max(A // C, B // D)

print(L - day)