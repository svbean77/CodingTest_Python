#2072 홀수만 더하기

T = int(input())

for test_case in range(1, T + 1):
    sum = 0
    numLst = list(map(int, input().split()))
    for num in numLst:
        if num % 2 != 0:
            sum += num

    print('#{0} {1}'.format(test_case, sum))