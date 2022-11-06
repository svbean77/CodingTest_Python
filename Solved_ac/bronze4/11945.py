#11945 뜨거운 붕어빵

N, M = map(int, input().split())

for _ in range(N):
    shape = list(input())

    for i in range(M // 2):
        shape[i], shape[M - 1 - i] = shape[M - 1 - i], shape[i]

    for item in shape:
        print(item, end = "")
    print()
