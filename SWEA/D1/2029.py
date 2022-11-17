#2029 몫과 나머지 출력하기

T = int(input())

for idx in range(1, T + 1):
    a, b = map(int, input().split())

    print('#{} {} {}'.format(idx, a // b, a % b))