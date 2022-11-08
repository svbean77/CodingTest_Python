#2588 곱셈

A = int(input())
B = input()

lst = []

for i in range(3):
    lst.append(A * int(B[2 - i]))
    print(lst[i])

print(lst[0] + lst[1] * 10 + lst[2] * 100)