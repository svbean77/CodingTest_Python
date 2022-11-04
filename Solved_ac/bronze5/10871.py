#10871 X보다 작은 수

N, X = map(int, input().split())

lst = list(map(int, input().split()))

for num in lst:
    if(X > num):
        print(num, end = ' ')