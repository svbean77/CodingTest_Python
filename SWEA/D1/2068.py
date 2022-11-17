#2068 최대수 구하기

T = int(input())

for idx in range(1, T + 1):
    num = list(map(int, input().split()))

    print('#{0} {1}'.format(idx, max(num)))