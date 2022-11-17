#2063 중간값 찾기

T = int(input())
num = sorted(list(map(int, input().split())))

print(num[T // 2])