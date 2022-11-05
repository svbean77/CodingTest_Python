#2573 세수정렬

lst = list(map(int, input().split()))

for _ in range(3):
    print(min(lst), end = ' ')
    lst.remove(min(lst))

