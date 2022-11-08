#10817 세 수

A, B, C = map(int, input().split())

#방법 1
#lst.sort()
#print(lst[1])

#방법 2
if max(A, B, C) == A:
    if B > C:
        print(B)
    else:
        print(C)

elif max(A, B, C) == B:
    if A > C:
        print(A)
    else:
        print(C)

else:
    if A > B:
        print(A)
    else:
        print(B)